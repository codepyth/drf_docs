from django.urls import path
from .views import (
    TodoListApiView,
    CreateMobileApiView,
)

urlpatterns = [
    path('all_mobilez/', TodoListApiView.as_view()),
    path('create_mobilez/', CreateMobileApiView.as_view()),
]