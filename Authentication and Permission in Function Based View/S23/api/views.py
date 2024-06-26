from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerialzer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, pk=None):
    if request.method == 'GET':
      id = pk
      if id is not None:
         stu = Student.objects.get(id=id)
         serializer = StudentSerialzer(stu)
         return Response(serializer.data)
      stu = Student.objects.all()
      serializer = StudentSerialzer(stu, many = True)
      return Response(serializer.data)
    
    if request.method == 'POST':
       serializer = StudentSerialzer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
       id = pk
       stu = Student.objects.get(pk=id)
       serializer = StudentSerialzer(stu, data= request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg': 'data Updated'})
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
       id = pk
       stu = Student.objects.get(pk=id)
       serializer = StudentSerialzer(stu, data= request.data, partial = True)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Partial data Updated'})
       return Response(serializer.errors)
    
    if request.method == 'DELETE':  
       id = pk
       stu = Student.objects.get(pk=id) 
       stu.delete()
       return Response({'msg': 'data Deleted'})
       

