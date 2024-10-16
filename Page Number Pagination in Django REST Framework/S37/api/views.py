from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(APIView):
    serializer_class = StudentSerializer
    def post(self, request, *args, **kwargs):
        # Form data handled by request.data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,pk=None,format=None):
      id = pk
      stu = Student.objects.get(pk=id)
      serializer = StudentSerializer(stu, data= request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({'msg': 'data Updated'})
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

