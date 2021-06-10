from django.shortcuts import render
from django.views.generic import ListView
from .models import Student
# Create your views here.

class studentlist(ListView):
    model=Student
    template_name='data.html'