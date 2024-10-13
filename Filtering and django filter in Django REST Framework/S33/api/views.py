from django.shortcuts import render
from .serializers import StudentSerialzer
from .models import Student
from rest_framework.generics import ListAPIView
# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby =user)

'''
এই কোডটি Django Rest Framework ব্যবহার করে একটি API ভিউ তৈরি করছে, যেটি ডাটাবেস থেকে Student মডেলের তথ্য লিস্ট আকারে রিটার্ন করবে। নিচে লাইন-বাই-লাইন ব্যাখ্যা দেওয়া হলো:

1. from .serializers import StudentSerialzer
StudentSerializer কে ইমপোর্ট করা হচ্ছে। এটি একটি সিরিয়ালাইজার, যা মডেলের ডাটা JSON বা অন্য ফরম্যাটে রূপান্তর করতে ব্যবহৃত হয়।
2. from .models import Student
Student মডেলটিকে ইমপোর্ট করা হচ্ছে, যেখানে শিক্ষার্থীদের তথ্য সংরক্ষণ করা হয়।
3. from rest_framework.generics import ListAPIView
ListAPIView ক্লাসটি ব্যবহার করা হচ্ছে, যেটি একটি রেডি-মেড ভিউ ক্লাস। এটি ডাটাবেস থেকে ডাটা লিস্ট আকারে রিটার্ন করতে ব্যবহৃত হয়।
4. class StudentList(ListAPIView):
StudentList নামে একটি ভিউ ক্লাস তৈরি করা হয়েছে, যেটি ListAPIView থেকে ইনহেরিট করেছে।
5. queryset = Student.objects.all()
এখানে queryset-এ Student মডেলের সব তথ্য ফিল্টার ছাড়া রিটার্ন করার জন্য উল্লেখ করা হয়েছে।
6. serializer_class = StudentSerialzer
serializer_class-এ StudentSerializer সেট করা হয়েছে, যেটি ডাটাবেসের ডাটা JSON ফরম্যাটে রূপান্তর করবে।
7. def get_queryset(self):
get_queryset() মেথডটি ব্যবহার করে আমরা queryset-এ কাস্টম ফিল্টার লাগাতে পারি। এখানে ফিল্টার করা হচ্ছে, যেন শুধু লগইন করা ব্যবহারকারীর সাথে সম্পর্কিত শিক্ষার্থীদের তথ্য রিটার্ন হয়।
8. user = self.request.user
request.user দিয়ে লগইনকৃত ব্যবহারকারীকে পাওয়া হচ্ছে।
9. return Student.objects.filter(passby=user)
Student মডেল থেকে passby নামে একটি ফিল্ডের ভ্যালু user-এর সমান হলে সেই শিক্ষার্থীদের তথ্য রিটার্ন করা হচ্ছে।
সংক্ষেপে:
এই ভিউটি এমন একটি API তৈরি করে যা শুধুমাত্র সেই শিক্ষার্থীদের তথ্য দেখাবে, যাদের passby ফিল্ডের মান লগইনকৃত ব্যবহারকারীর সাথে মিলে। অর্থাৎ, একজন ব্যবহারকারী শুধুমাত্র নিজের সাথে সম্পর্কিত শিক্ষার্থীদের তথ্য দেখতে পারবে।

'''    
    