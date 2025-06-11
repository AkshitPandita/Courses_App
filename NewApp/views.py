from django.shortcuts import render
from .models import Courses
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def New_app_view(request):
    # Logic for your view goes here
    courses= Courses.objects.all()
    return render(request, 'NewApp/new_app.html',{'courses': courses})

@login_required(login_url='login')
def course_detail(request, course_id):
    # Logic to get course details by ID
    course = Courses.objects.get(id=course_id)
    return render(request, 'NewApp/course_detail.html', {'course': course})
