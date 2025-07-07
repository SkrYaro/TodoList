from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from TodoList.models import Task, Profile


# Create your views here.

def main(request):
    tasks = Task.objects.all()
    profile = get_object_or_404(Profile,name = request.user)
    context = {"tasks": tasks,
               "profile":profile,

            }
    return render(request,template_name='profile/main.html',context=context)
