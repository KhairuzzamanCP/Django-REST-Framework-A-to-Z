from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .myPaginations import MyPageNumberPagination
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination

'''
StudentList একটি Django Rest Framework (DRF)-এর API ভিউ যা ListAPIView থেকে উত্তরাধিকার (inherit) করছে। এই ক্লাসের কাজ হলো ডাটাবেজ থেকে সব ছাত্রদের তালিকা আনা এবং পেজিনেশনসহ রেসপন্সে দেখানো। নিচে প্রতিটি অংশের ব্যাখ্যা দেওয়া হলো:

queryset = Student.objects.all()

এটি ডাটাবেজের Student মডেল থেকে সব ছাত্রদের তথ্য নিয়ে আসে।
queryset ডাটার সেট যা API-এর মাধ্যমে দেখানো হবে।
serializer_class = StudentSerializer

StudentSerializer ডাটা সিরিয়ালাইজ করে, অর্থাৎ ডাটাবেজের অবজেক্টগুলোকে JSON ফরম্যাটে রূপান্তর করে পাঠায়, যাতে API-এর মাধ্যমে ক্লায়েন্ট সেগুলো বুঝতে পারে।
pagination_class = MyPageNumberPagination

এই ভিউতে আমরা আগে তৈরি করা MyPageNumberPagination পেজিনেশন ক্লাসটি ব্যবহার করছি।
এর ফলে API রেসপন্সে ছাত্রদের তালিকা পেজ ভিত্তিক আকারে দেখানো হবে, এবং ব্যবহারকারী URL প্যারামিটার দিয়ে পেজ নম্বর ও রেকর্ড সংখ্যা নিয়ন্ত্রণ করতে পারবে।
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

