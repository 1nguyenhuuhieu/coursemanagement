from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('register/', views.register, name='register')
]
