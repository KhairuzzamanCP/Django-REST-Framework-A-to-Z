from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerialzer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
'''
   def get(self, request, pk = None, format = None):
   
   এই কোডটি একটি ফাংশন ভিউ ক্লাসের মেথড ডেফিনিশন প্রদর্শন করে, যা একটি HTTP GET অনুরোধের জন্য প্রস্তুতি করে। এই মেথডের প্যারামিটার হিসেবে নিম্নলিখিত প্যারামিটারগুলি রয়েছে:

   self: এটি পাইথনের সেলফ অবজেক্ট, যা অবশ্যই মেথডের প্রথম প্যারামিটার হতে হবে।
   request: এটি HTTP অনুরোধের সম্পর্কিত তথ্য নিয়ে আসে, যেমন পারামিটার, হেডার, বডি ইত্যাদি।
   pk: এটি একটি প্রাইমারি কী (অথবা "প্রাইমারি কে" নির্দেশ করে) যা ব্যবহৃত হয় পরিমাণ সংখ্যার ডেটা নির্দেশ করতে হয়। এই মেথড বিশেষভাবে একটি নির্দিষ্ট এন্টিটির (যেমন একটি ডেটাবেস রেকর্ড) ডেটা প্রাপ্ত করতে ব্যবহৃত হয়। এটি একটি অপশনাল প্যারামিটার, এটি প্রয়োজনে বা অপ্সনাল হতে পারে।
   format: এটি অনুরোধের ফরম্যাট নির্দেশ করে, যেমন JSON, XML ইত্যাদি। এটি অপশনাল প্যারামিটার।
'''

class StudentAPI(APIView):
   def get(self, request, pk=None, format=None):
      id = pk
      if id is not None:
         stu = Student.objects.get(id=id)
         serializer = StudentSerialzer(stu)
         return Response(serializer.data)
      stu = Student.objects.all()
      serializer = StudentSerialzer(stu, many = True)
      return Response(serializer.data)
   
   def post(self,request,format=None):
      serializer = StudentSerialzer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def put(self, request,pk=None,format=None):
      id = pk
      stu = Student.objects.get(pk=id)
      serializer = StudentSerialzer(stu, data= request.data)
      if serializer.is_valid():
          serializer.save()
          return Response({'msg': 'data Updated'})
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def patch(self,request,pk=None,format=None):
      id = pk
      stu = Student.objects.get(pk=id)
      serializer = StudentSerialzer(stu, data= request.data, partial = True)
      if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Partial data Updated'})
      return Response(serializer.errors)
      
   
   def delete(self, request,pk=None,format=None):
      id = pk
      stu = Student.objects.get(pk=id) 
      stu.delete()
      return Response({'msg': 'data Deleted'})





      


# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def student_api(request, pk=None):
#     if request.method == 'GET':
#       id = pk
#       if id is not None:
#          stu = Student.objects.get(id=id)
#          serializer = StudentSerialzer(stu)
#          return Response(serializer.data)
#       stu = Student.objects.all()
#       serializer = StudentSerialzer(stu, many = True)
#       return Response(serializer.data)
    
#     if request.method == 'POST':
#        serializer = StudentSerialzer(data=request.data)
#        if serializer.is_valid():
#           serializer.save()
#           return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PUT':
#        id = pk
#        stu = Student.objects.get(pk=id)
#        serializer = StudentSerialzer(stu, data= request.data)
#        if serializer.is_valid():
#           serializer.save()
#           return Response({'msg': 'data Updated'})
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'PATCH':
      #  id = pk
      #  stu = Student.objects.get(pk=id)
      #  serializer = StudentSerialzer(stu, data= request.data, partial = True)
      #  if serializer.is_valid():
      #     serializer.save()
      #     return Response({'msg':'Partial data Updated'})
      #  return Response(serializer.errors)
    
#     if request.method == 'DELETE':  
#        id = pk
#        stu = Student.objects.get(pk=id) 
#        stu.delete()
#        return Response({'msg': 'data Deleted'})
       

