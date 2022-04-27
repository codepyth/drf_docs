from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import MyUser
# Create your views here.


@permission_classes([AllowAny])
@api_view(['POST'])
def register(request):
    first_name = request.data['first_name'] if 'first_name' in request.data else None
    last_name = request.data['last_name'] if 'last_name' in request.data else None
    email = request.data['email'] if 'email' in request.data else None
    username = request.data['username'] if 'username' in request.data else None
    password = request.data['password'] if 'password' in request.data else None

    if not first_name:
        return Response({"success": False, 'response': 'first_name is required for Sign Up!'},
                        status=status.HTTP_400_BAD_REQUEST)

    if not email:
        return Response({"success": False, 'response': 'email is required for Sign Up!'},
                        status=status.HTTP_400_BAD_REQUEST)

    if not username:
        return Response({"success": False, 'response': 'username required for Sign Up!'})
    try:
        username = MyUser.objects.get(username=username)
        return Response({"success": False, 'response': 'Username already taken!'})
    except:
        pass

    try:
        email = MyUser.objects.get(email=email)
        return Response({"success": False, 'response': 'Email already exists. Use new one!'},
                        status=status.HTTP_400_BAD_REQUEST)
    except:
        pass

    if not password:
        return Response({"success": False, 'response': 'password is required!'},
                        status=status.HTTP_400_BAD_REQUEST)

    if not password:
        return Response({'response': 'password required and minimum 10 Characters!'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = MyUser.objects.create(first_name=first_name, last_name=last_name, email=email, username=username,
                                 password=password)
    user.set_password(password)
    user.save()

    return Response({"success": True, 'status': status.HTTP_201_CREATED, 'message': 'Congratulations, Registered!'})