from .models import Student
from .serializers import StudentSerialzer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
'''
class StudentModelViewSet(viewsets.ModelViewSet):

এখানে StudentModelViewSet নামক একটি ক্লাস তৈরি করা হয়েছে যা ModelViewSet থেকে উত্তরাধিকার (inheritance) করছে। ModelViewSet হলো Django Rest Framework-এর একটি ভিউসেট যা স্বয়ংক্রিয়ভাবে Student মডেলের জন্য CRUD অপারেশনগুলো পরিচালনা করতে পারে।
queryset = Student.objects.all()

এই লাইনটি Student মডেলের সকল অবজেক্টের একটি কুয়েরিসেট তৈরি করছে। অর্থাৎ, ডাটাবেসে থাকা সমস্ত Student রেকর্ড এই কুয়েরিসেটে অন্তর্ভুক্ত হবে।
serializer_class = StudentSerialzer

এই লাইনটি StudentSerialzer ক্লাসটি নির্ধারণ করে যা Student মডেলের ডাটা সিরিয়ালাইজ করার জন্য ব্যবহৃত হবে। অর্থাৎ, Student মডেলের ডাটা কিভাবে JSON বা অন্যান্য ফরম্যাটে রূপান্তরিত হবে তা এই সিরিয়ালাইজার দ্বারা নির্ধারিত হবে।
authentication_classes = [JWTAuthentication]

এই লাইনটি নির্দেশ করে যে এই ভিউসেটের জন্য JWT (JSON Web Token) প্রমাণীকরণ ব্যবহৃত হবে। অর্থাৎ, ব্যবহারকারীদেরকে JWT টোকেনের মাধ্যমে প্রমাণীকৃত হতে হবে যাতে তারা এই API-এর মাধ্যমে Student মডেলের ডাটা অ্যাক্সেস করতে পারে।
permission_classes = [IsAuthenticated]

এই লাইনটি নির্দেশ করে যে শুধুমাত্র প্রমাণীকৃত ব্যবহারকারীরা (authenticated users) এই API এন্ডপয়েন্ট ব্যবহার করতে পারবে। অর্থাৎ, যদি ব্যবহারকারী লগইন না করে থাকে, তবে তারা এই ভিউসেটে অ্যাক্সেস পাবে না।
এই সেটআপটি নিরাপদ এবং প্রমাণীকৃত অ্যাক্সেসের জন্য খুবই উপযুক্ত যেখানে আপনি শুধুমাত্র অথেনটিকেটেড ব্যবহারকারীদেরকেই ডাটাবেসের Student মডেলের উপর CRUD অপারেশন করতে দিতে চান।
'''


    

   




       

