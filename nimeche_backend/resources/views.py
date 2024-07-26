from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Blog, Material


# Create your views here.
class BlogView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MaterialView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MaterialDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        material = get_object_or_404(Material, pk=pk)
        serializer = MaterialSerializer(material)
        return Response(serializer.data, status=status.HTTP_200_OK)