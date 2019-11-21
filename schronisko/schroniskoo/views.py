from django.shortcuts import render
from .models import *
from .serializers import  *
from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
def index(request):
    return HttpResponse("Hello homie .")



