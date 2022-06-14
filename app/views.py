from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import StoreImg
from .serializers import StoreImgSerializer

# Create your views here.


class ImagesViewset(viewsets.ModelViewSet):
    serializer_class = StoreImgSerializer
    # http_method_names = ["post", "get", ]
    queryset = StoreImg.objects.all()
