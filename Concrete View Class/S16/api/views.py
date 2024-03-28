# Generic API View and Model Mixin
from .models import Student
from .serializers import StudentSerialzer 
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
    
'''
এই কোডটি আবারও Django REST Framework এর একটি view ক্লাস নির্দেশ করে। StudentListCreate নামের ক্লাসটি ListCreateAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি একটি HTTP GET রিকোয়েস্টের জন্য একটি তালিকা অবজেক্টের সিলেকশন করে এবং একটি HTTP POST রিকোয়েস্টের জন্য নতুন স্টুডেন্ট তৈরি করে।
'''
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer


'''

এই কোডটি ডিজাঙ্গো রেস্ট ফ্রেমওয়ার্কের একটি view ক্লাস নির্দেশ করে। StudentRetrieveUpdateDestroy নামের ক্লাসটি RetrieveUpdateDestroyAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি একটি HTTP GET রিকোয়েস্টের জন্য নির্দিষ্ট ছাত্র অবজেক্ট প্রদর্শন করে, HTTP PUT বা PATCH রিকোয়েস্টের জন্য সেই ছাত্র অবজেক্ট আপডেট করে, এবং HTTP DELETE রিকোয়েস্টের জন্য ঐ ছাত্র অবজেক্ট মুছে ফেলে।

queryset প্রপার্টিতে, এটি সমস্ত Student অবজেক্ট সিলেক্ট করে। এটি ব্যবহৃত হয়েছে যেন একটি নির্দিষ্ট অবজেক্ট প্রদর্শন করা, পরবর্তীতে অবজেক্ট আপডেট করা এবং অবজেক্ট মুছে ফেলা যায়।
'''
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    


   




       

