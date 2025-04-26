from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]