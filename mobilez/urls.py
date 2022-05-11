from django.urls import path
from .views import (
    MobileListApiView,
    MobileCreateApiView,
    MobileDetailApiView
)

urlpatterns = [
    path('all_mobilez/', MobileListApiView.as_view()),
    path('create_mobilez/', MobileCreateApiView.as_view()),
    path('detail_mobilez/<int:id>/', MobileDetailApiView.as_view()),
]