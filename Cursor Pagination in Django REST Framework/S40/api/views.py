from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .myPaginations import MyCursorPagination
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination

'''
StudentList ক্লাস
এটি ListAPIView থেকে ইনহেরিট করেছে, যা DRF-এ এমন ভিউ তৈরি করতে ব্যবহৃত হয় যেখানে শুধু লিস্ট করা হয় বা রিড-অনলি ডেটা প্রদর্শন করা হয়।
2. queryset = Student.objects.all()
Student মডেলের সমস্ত রেকর্ড ডাটাবেস থেকে নিয়ে আসা হচ্ছে। অর্থাৎ, Student মডেলের প্রতিটি ইনস্ট্যান্স এই ভিউতে দেখানো যাবে।
3. serializer_class = StudentSerializer
ডাটাগুলোকে JSON বা অন্য ফরম্যাটে রূপান্তর করতে StudentSerializer ব্যবহার করা হচ্ছে। Serializer ডাটাকে serialize (রূপান্তর) করে পাঠায় এবং চাইলে validate-ও করতে পারে।
4. pagination_class = MyCursorPagination
এখানে প্যাগিনেশন হিসেবে আমরা MyCursorPagination ব্যবহার করেছি, যেটি আমরা আগের কোডে তৈরি করেছিলাম।
প্রতি পেজে ৫টি করে Student রেকর্ড দেখাবে এবং name ফিল্ডের ক্রমানুসারে সাজাবে।
এই কোডের কার্যকারিতা:
যখন এই API-তে কেউ রিকোয়েস্ট পাঠাবে, তখন CursorPagination ব্যবহারের মাধ্যমে একবারে ৫টি রেকর্ড পাঠানো হবে।
পরবর্তী পৃষ্ঠার জন্য response-এ একটি cursor থাকবে, যা দিয়ে পরের ডেটাগুলো দেখতে পারবে।
এটা API-এর পারফরম্যান্স উন্নত করতে সাহায্য করে, বিশেষ করে যখন ডেটাবেসে অনেক রেকর্ড থাকে।

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

