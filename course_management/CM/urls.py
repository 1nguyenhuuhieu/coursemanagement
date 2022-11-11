from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('remove_cart/<int:id>/', views.remove_cart, name='remove_cart'),
    path('pay/', views.pay, name='pay'),
    path('my-courses/', views.my_courses, name='my-courses'),
    path('courses/', views.courses, name='courses'),
    path('my-course-detail/<int:id>/', views.my_course_detail, name='my_course_detail'),
    path('video/<int:id>', views.video, name='video'),
    path('search-data/', views.search_data, name='search_data'),
    path('search-result/', views.search, name='search_result'),
]
