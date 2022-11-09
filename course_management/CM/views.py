from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }

    return render(request, 'index.html', context)

def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }

    return render(request, 'courses_all.html', context)

def course_detail(request, id):
    course = get_object_or_404(Course, pk=id)
  
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = UserCourseForm(request.POST)

            if form.is_valid():
                form.instance.user = request.user
                form.instance.course = course
                form.save()
                if "redirectCart" in request.POST:
                    return redirect('cart')
                else:
                    return redirect('course_detail', id)
        else:
            return redirect('login')
    else:
        form = UserCourseForm(
            initial={
                'user': request.user,
                'course': course,
            }
        )
    
    context = {
        'course': course,
        'form': form
    }
    return render(request, 'course_detail.html', context)

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})

@login_required
def cart(request):
    carts = UserCourse.objects.filter(user=request.user).exclude(status='purchased')
    carts_price = sum(cart.course.price for cart in carts)
    context = {
        'carts': carts,
        'carts_price': carts_price
    }

    return render(request, 'cart.html', context)

@login_required
def remove_cart(request, id):
    user_course = get_object_or_404(UserCourse, pk=id, user=request.user)
    user_course.delete()
    return redirect('cart')

@login_required
def pay(request):
    user_course = UserCourse.objects.filter(user=request.user, status='added')
    if user_course:
        for course in user_course:
            update_course = UserCourse.objects.get(pk=course.id)
            update_course.status = 'waiting'
            update_course.save()

    return redirect('index')

@login_required
def my_courses(request):
    courses = UserCourse.objects.filter(user=request.user, status='purchased')
    context = {
        'courses': courses
    }

    return render(request, 'my-courses.html', context)

@login_required
def my_course_detail(request, id):
    course = get_object_or_404(UserCourse, pk=id)
    videos = Video.objects.filter(courses=course.course)

    context = {
        'course': course,
        'videos': videos
    }

    return render(request, 'my-course-detail.html', context)

@login_required
def video(request, id):
    video = get_object_or_404(Video, pk=id)

    context = {
        'video': video
    }

    return render(request, 'video.html', context)