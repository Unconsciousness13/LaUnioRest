from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from launio.club.models import Gymnast
from .serializers import GymnastSerializer
from launio.api import serializers
from rest_framework import generics



class GymnastList(generics.ListCreateAPIView):
    queryset = Gymnast.objects.all()
    serializer_class = GymnastSerializer
    

class GymnastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gymnast.objects.all()
    serializer_class = GymnastSerializer

    
