from django.urls import path
from . import views

urlpatterns = [
    path('gymnasts/', views.GymnastList.as_view()),
    path('gymnast/<int:pk>/', views.GymnastDetail.as_view()),
    
]

