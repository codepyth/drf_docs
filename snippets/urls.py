from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('get_user/', get_user, name='get_user'),
    path('add_employee/', add_employee, name='add_employee'),
    path('get_all_employees/', get_all_employees, name='get_all_employees'),
    path('filter_employees/', filter_employees, name='filter_employees'),
    path('get_signle_employee/<int:id>/', get_signle_employee, name='get_signle_employee'),
    path('update_employee/<int:id>/', update_employee, name='update_employee'),
    path('delete_employee/<int:id>/', delete_employee, name='delete_employee'),
]