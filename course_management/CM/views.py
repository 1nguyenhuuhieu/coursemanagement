from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }

    return render(request, 'index.html', context)

def course_detail(request, id):
    course = get_object_or_404(Course, pk=id)
    context = {
        'course': course
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