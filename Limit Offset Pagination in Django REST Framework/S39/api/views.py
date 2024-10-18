from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .myPaginations import MyOffsetPagination
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyOffsetPagination

'''
এই কোডটি Django Rest Framework-এ একটি API ভিউ তৈরি করার জন্য ব্যবহার করা হয়েছে, যেখানে ListAPIView ব্যবহার করে শিক্ষার্থীদের লিস্ট দেখানো হচ্ছে।

class StudentList(ListAPIView):
এই ক্লাসটি ListAPIView এক্সটেন্ড করে শিক্ষার্থীদের তথ্য দেখানোর জন্য একটি ভিউ তৈরি করে।

queryset = Student.objects.all():
Student মডেলের সব ডেটা কুয়েরি করে রিটার্ন করবে।

serializer_class = StudentSerializer:
এই ভিউতে ডেটা কীভাবে দেখানো হবে তা নির্ধারণ করার জন্য StudentSerializer ব্যবহার করা হয়েছে।

pagination_class = MyOffsetPagination:
আগের তৈরি MyOffsetPagination পেজিনেশন ক্লাসটি এখানে ব্যবহার করা হয়েছে, যাতে শিক্ষার্থীদের তালিকাটি পেজিনেট করা যায়।
'''

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

