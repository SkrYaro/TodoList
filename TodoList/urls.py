from django.urls import path

from TodoList import views



urlpatterns = [
    path('',views.main, name = 'main'),
]