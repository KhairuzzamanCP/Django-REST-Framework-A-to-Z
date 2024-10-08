from .models import Student
from .serializers import StudentSerialzer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.throttling import JackRateTHrottle  
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # throttle_classes = [AnonRateThrottle,JackRateTHrottle]
    
'''
এই কোডটি Django Rest Framework ব্যবহার করে একটি StudentModelViewSet তৈরি করেছে। এটি মূলত একটি API তৈরি করার জন্য ব্যবহার করা হয় যেখানে Student মডেলের সমস্ত ডেটা দেখানো, যোগ করা, সম্পাদনা করা এবং মুছে ফেলার কাজ করা যাবে। এখানে প্রতিটি অংশের ব্যাখ্যা বাংলায় দেওয়া হলো:

Imports:

Student, StudentSerialzer: Student মডেল এবং এর জন্য তৈরি করা Serializer।
viewsets.ModelViewSet: এটি ডিফল্ট API ভিউ তৈরি করার জন্য ব্যবহৃত হয় যা চারটি CRUD অপারেশন (Create, Read, Update, Delete) সমর্থন করে।
IsAuthenticatedOrReadOnly, IsAuthenticated: এগুলি হলো permission ক্লাস, যা নির্ধারণ করে কে এই API-তে অ্যাক্সেস করতে পারবে।
SessionAuthentication: এটি session ভিত্তিক authentication সিস্টেম।
AnonRateThrottle, UserRateThrottle: থ্রটলিং ক্লাস, যা API অ্যাক্সেসের হার নিয়ন্ত্রণ করে।
JackRateTHrottle: কাস্টম থ্রটলিং ক্লাস যা 'api.throttling' থেকে এসেছে।
StudentModelViewSet ক্লাস:

queryset = Student.objects.all(): এটি ডাটাবেজ থেকে Student মডেলের সমস্ত রেকর্ড নিয়ে আসে।
serializer_class = StudentSerialzer: Student মডেলের ডেটা সিরিয়ালাইজ করার জন্য এই Serializer ব্যবহার করা হবে।
authentication_classes = [SessionAuthentication]: এটি নির্ধারণ করে যে এই API তে সেশনের মাধ্যমে Authentication করা হবে।
permission_classes = [IsAuthenticatedOrReadOnly]: এটি নির্ধারণ করে যে অ্যাক্সেসের জন্য ইউজারকে অথেনটিকেটেড হতে হবে বা শুধুমাত্র রিড-অনলি পারমিশন থাকবে।
throttle_classes = [AnonRateThrottle, UserRateThrottle]: এটি থ্রটলিং কন্ট্রোল করে, যেখানে Anonymous ইউজার এবং Authenticated ইউজারের জন্য আলাদা আলাদা রেট লিমিট নির্ধারণ করা হয়েছে।
বিকল্পভাবে:

কিছু লাইন কমেন্ট আকারে রাখা হয়েছে। যেমন, যদি permission_classes = [IsAuthenticated] ব্যবহার করা হয়, তাহলে শুধুমাত্র অথেনটিকেটেড ইউজার API ব্যবহার করতে পারবে।
JackRateTHrottle কাস্টম থ্রটলিং ক্লাসও ব্যবহার করা যেতে পারে।
'''



    

   




       

