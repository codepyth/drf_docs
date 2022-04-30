from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import MyUser
from .serializers import *
from rest_framework.decorators import api_view

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
    
    is_staff = True
    user = MyUser.objects.create(first_name=first_name, last_name=last_name, email=email, is_staff=is_staff, username=username,
                                 password=password)
    user.set_password(password)
    user.save()

    return Response({"success": True, 'status': status.HTTP_201_CREATED, 'message': 'Congratulations, Registered!'})


@api_view(['POST'])
def add_employee(request):
    if request.method == 'POST':
        serializers = EmployeeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_employees(request):
    if request.method == 'GET':
        emp = employee.objects.all()
        serializers = EmployeeSerializer(emp,many=True)
        return Response(serializers.data)


@api_view(['GET'])
def get_signle_employee(request, id):
    if request.method == 'GET':
        try:
            emp = employee.objects.get(id=id)
            serializers = EmployeeSerializer(emp)
            return Response(serializers.data)
        except employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_employee(request,id):
    obj = employee.objects.get(id=id)
    serializer = EmployeeSerializer(obj , data=request.data, partial = True)

    if serializer.is_valid():
            serializer.save()
            return Response({"msg" : "data updated"})
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete_employee(request,id):
    if request.method == "DELETE":
        obj = employee.objects.get(id=id)
        obj.delete()
        return Response({ "msg" : "data deleted"  })


