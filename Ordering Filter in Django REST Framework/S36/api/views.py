from django.shortcuts import render
from .serializers import StudentSerialzer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    filter_backends =[OrderingFilter]
    ordering_fields =['name', 'city']
    
'''
render: Django-তে পেজ রেন্ডার করার জন্য ব্যবহৃত হয় (যদিও এই কোডে render ব্যবহার করা হয়নি)।
StudentSerialzer: Student মডেলের ডেটা JSON ফরম্যাটে রূপান্তর করার জন্য এই সিরিয়ালাইজার ব্যবহার করা হবে।
Student: Student মডেল থেকে ডেটা নেওয়ার জন্য এটি ব্যবহার করা হয়েছে।
ListAPIView: এটি একটি জেনেরিক ক্লাস, যা read-only API তৈরি করতে সাহায্য করে (যেমন, শুধুমাত্র লিস্ট দেখাবে)।
DjangoFilterBackend: ডেটার উপরে ফিল্টারিং করতে এই ব্যাকএন্ড ব্যবহার করা হয়েছে।
class StudentList(ListAPIView):

ListAPIView ব্যবহার করে এই ভিউ-তে শুধু ডেটার তালিকা দেখানো হবে।
এখানে আমরা Student মডেলের সব ডেটা লিস্ট আকারে পাব।
queryset = Student.objects.all():

queryset দ্বারা Student মডেলের সব অবজেক্টগুলোকে ডাটাবেস থেকে আনা হচ্ছে।
serializer_class = StudentSerialzer:

এই ভিউতে ডেটা সিরিয়ালাইজ করার জন্য StudentSerialzer ব্যবহার করা হবে, যাতে ডেটা JSON ফরম্যাটে রূপান্তরিত হয়।
filter_backends = [DjangoFilterBackend]:

এখানে DjangoFilterBackend ব্যবহার করে ভিউতে ফিল্টার করার সুবিধা যোগ করা হয়েছে।
filterset_fields = ['city', 'name']:

এখানে উল্লেখ করা হয়েছে কোন ফিল্ডগুলো ফিল্টার করা যাবে।
অর্থাৎ, city এবং name ফিল্ডের ওপর ভিত্তি করে ফিল্টার করে ডেটা দেখা যাবে।
সংক্ষেপে বললে:

এই কোডটি একটি API ভিউ তৈরি করে যা Student মডেলের ডেটার তালিকা দেখাবে। ব্যবহারকারী চাইলে city বা name ফিল্ড অনুযায়ী ফিল্টার করে ডেটা দেখতে পারবে।

সংক্ষেপে বললে:
এই কোডটি একটি API ভিউ তৈরি করে যা Student মডেলের ডেটার তালিকা দেখাবে। ব্যবহারকারী চাইলে city বা name ফিল্ড অনুযায়ী ফিল্টার করে ডেটা দেখতে পারবে।
'''


