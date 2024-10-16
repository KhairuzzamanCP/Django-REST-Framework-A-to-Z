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
class StudentList(ListAPIView): এই ক্লাসটি তৈরি করা হয়েছে ListAPIView ভিউ ব্যবহার করে, যা Student মডেলের সব ডাটা লিস্ট আকারে দেখাবে।

queryset = Student.objects.all(): এটি Student মডেলের সব তথ্য ডাটাবেজ থেকে এনে একটি কুয়েরি সেট তৈরি করছে।

serializer_class = StudentSerialzer: মডেলের ডাটাকে JSON বা অন্য কোনো ফরম্যাটে রূপান্তরের জন্য StudentSerialzer ব্যবহার করা হচ্ছে।

filter_backends = [OrderingFilter]: ডাটাকে নির্দিষ্ট ক্রমে সাজানোর জন্য OrderingFilter ব্যবহার করা হয়েছে।

ordering_fields = ['name', 'city']: এখানে ব্যবহারকারী name এবং city অনুযায়ী ডাটাগুলোকে অর্ডার করে দেখতে পারবে। উদাহরণস্বরূপ, /students?ordering=name এভাবে API কল করলে name অনুযায়ী সাজানো ডাটা পাওয়া যাবে।

সারসংক্ষেপে
এই কোডটি একটি API তৈরি করে, যেখানে Student মডেলের ডাটা লিস্ট আকারে দেখানো হবে এবং ব্যবহারকারী চাইলে name বা city ফিল্ড অনুযায়ী ডাটাগুলো সাজিয়ে দেখতে পারবে।
'''
