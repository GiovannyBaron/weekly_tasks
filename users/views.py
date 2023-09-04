from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.db.models.functions import Random
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import LoginForm


import json

from .models import User


@api_view(['POST'])
def user_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("tasks/")
    else:
        return Response({'message': 'Inicio de sesión fallido'}, status=401)


@api_view(['GET'])
def sign_out(request):
    logout(request)
    return Response({'message': 'Ha terminado la sesión'})
