# Generic API View and Model Mixin
from .models import Student
from .serializers import StudentSerialzer 
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

'''
এই কোডটি একটি Django REST Framework view ক্লাস দেখাচ্ছে। StudentList নামক এই ক্লাসটি ListAPIView ক্লাস থেকে সাবক্লাস করে। এটি একটি HTTP GET রিকোয়েস্ট এর জন্য সরবরাহ করে একটি তালিকা অবজেক্টের সিলেকশন।

queryset প্রপার্টির মাধ্যমে, এটি সমস্ত Student অবজেক্ট সিলেক্ট করে। Student মডেলের একটি উদাহরণ হতে পারে যা এই মডেলের ডেটাবেস টেবিলের নাম।

serializer_class প্রপার্টিতে, এটি ডেটা সিরিয়ালাইজ করার জন্য ব্যবহৃত সিরিয়ালাইজার ক্লাস নির্দেশ করে। সিরিয়ালাইজার ক্লাসটি ডেটা বিষয়বস্তুকে JSON ফরম্যাটে রূপান্তর করে এবং পার্স করে। এখানে, StudentSerializer হতে পারে সেরা উদাহরণ একটি সিরিয়ালাইজার ক্লাস যা Student মডেলের ডেটা সিরিয়ালাইজ করে।
'''
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    

'''
এই কোডটি আবারও Django REST Framework এর একটি view ক্লাস নির্দেশ করে। StudentCreate নামের ক্লাসটি CreateAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি HTTP POST রিকোয়েস্টের জন্য একটি নতুন স্টুডেন্ট তৈরি করে।
'''
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

'''
এই কোডটি আবারও Django REST Framework এর একটি view ক্লাস নির্দেশ করে। StudentRetrieve নামের ক্লাসটি RetrieveAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি HTTP GET রিকোয়েস্টের জন্য একটি নির্দিষ্ট স্টুডেন্ট অবজেক্ট প্রদর্শন করে।
'''
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

'''
এই কোডটি আবারও Django REST Framework এর একটি view ক্লাস নির্দেশ করে। StudentUpdate নামের ক্লাসটি UpdateAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি HTTP PUT অথবা PATCH রিকোয়েস্টের জন্য নির্দিষ্ট স্টুডেন্ট অবজেক্ট আপডেট করে।
'''
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

'''
এই কোডটি আবারও Django REST Framework এর একটি view ক্লাস নির্দেশ করে। StudentDestroy নামের ক্লাসটি DestroyAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি HTTP DELETE রিকোয়েস্টের জন্য নির্দিষ্ট স্টুডেন্ট অবজেক্ট মুছে ফেলে।
'''
class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
'''
এই কোডটি আবারও Django REST Framework এর একটি view ক্লাস নির্দেশ করে। StudentListCreate নামের ক্লাসটি ListCreateAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি একটি HTTP GET রিকোয়েস্টের জন্য একটি তালিকা অবজেক্টের সিলেকশন করে এবং একটি HTTP POST রিকোয়েস্টের জন্য নতুন স্টুডেন্ট তৈরি করে।
'''
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

'''
এই কোড Django REST Framework এর একটি view ক্লাস নির্দেশ করে। StudentRetrieveUpdate নামের ক্লাসটি RetrieveUpdateAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি HTTP GET রিকোয়েস্টের জন্য নির্দিষ্ট স্টুডেন্ট অবজেক্ট প্রদর্শন করে এবং HTTP PUT অথবা PATCH রিকোয়েস্টের জন্য সেই স্টুডেন্ট অবজেক্ট আপডেট করে।

queryset প্রপার্টিতে, এটি সমস্ত Student অবজেক্ট সিলেক্ট করে। এটি ব্যবহৃত হয়েছে কারণ RetrieveUpdateAPIView এর কাজ হলো একটি নির্দিষ্ট অবজেক্ট প্রদর্শন করা এবং পরবর্তীতে সেই অবজেক্টের আপডেট করা।
'''
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

'''
এই কোডটি ডিজাঙ্গো রেস্ট ফ্রেমওয়ার্কের একটি view ক্লাস নির্দেশ করে। StudentRetrieveDestroy নামের ক্লাসটি RetrieveDestroyAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি একটি HTTP GET রিকোয়েস্টের জন্য নির্দিষ্ট ছাত্র অবজেক্ট প্রদর্শন করে এবং HTTP DELETE রিকোয়েস্টের জন্য ঐ ছাত্র অবজেক্ট মুছে ফেলে।

queryset প্রপার্টিতে, এটি সমস্ত Student অবজেক্ট সিলেক্ট করে। এটি ব্যবহৃত হয়েছে যেন একটি নির্দিষ্ট অবজেক্ট প্রদর্শন করা এবং পরবর্তীতে এই অবজেক্ট মুছে ফেলা যায়।
'''    
class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer


'''

এই কোডটি ডিজাঙ্গো রেস্ট ফ্রেমওয়ার্কের একটি view ক্লাস নির্দেশ করে। StudentRetrieveUpdateDestroy নামের ক্লাসটি RetrieveUpdateDestroyAPIView ক্লাস থেকে সাবক্লাস করা হয়েছে। এটি একটি HTTP GET রিকোয়েস্টের জন্য নির্দিষ্ট ছাত্র অবজেক্ট প্রদর্শন করে, HTTP PUT বা PATCH রিকোয়েস্টের জন্য সেই ছাত্র অবজেক্ট আপডেট করে, এবং HTTP DELETE রিকোয়েস্টের জন্য ঐ ছাত্র অবজেক্ট মুছে ফেলে।

queryset প্রপার্টিতে, এটি সমস্ত Student অবজেক্ট সিলেক্ট করে। এটি ব্যবহৃত হয়েছে যেন একটি নির্দিষ্ট অবজেক্ট প্রদর্শন করা, পরবর্তীতে অবজেক্ট আপডেট করা এবং অবজেক্ট মুছে ফেলা যায়।
'''
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    


   




       

