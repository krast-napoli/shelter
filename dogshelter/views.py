#from django.shortcuts import render, get_object_or_404 - uncomment if you use only viewsets without routers
from rest_framework import viewsets
#from rest_framework.response import Response - uncomment if you use only viewsets without routers
from .models import Dogs
from .serializers import DogsSerializer

class DogsViewSet(viewsets.ModelViewSet):
    serializer_class = DogsSerializer
    queryset = Dogs.objects.all()

'''
uncomment if you use only viewsets without routers

class DogsView(viewsets.ViewSet):

    def list (self, request):
        queryset = Dogs.objects.all()
        serializer = DogsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve (self, request, pk=None):
        queryset = Dogs.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogsSerializer(user)
        return Response(serializer.data)
'''
