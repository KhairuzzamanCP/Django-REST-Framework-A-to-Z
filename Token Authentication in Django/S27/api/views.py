from .models import Student
from .serializers import StudentSerialzer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
  
    
'''
class StudentModelViewSet(viewsets.ModelViewSet):

এখানে StudentModelViewSet নামে একটি ক্লাস তৈরি করা হয়েছে যা viewsets.ModelViewSet থেকে উত্তরাধিকার (inheritance) লাভ করেছে।
viewsets.ModelViewSet একটি ডিফল্ট ভিউসেট ক্লাস যা সব ধরনের CRUD অপারেশন পরিচালনা করার জন্য ব্যবহার করা হয়।
queryset = Student.objects.all():

এখানে queryset নির্ধারণ করা হয়েছে যা Student মডেলের সমস্ত অবজেক্ট/ডেটা ধারণ করে।
Student.objects.all() Student মডেলের সমস্ত রেকর্ড/অবজেক্টকে রিটার্ন করে।
serializer_class = StudentSerialzer:

এই অংশে serializer_class নির্ধারণ করা হয়েছে যা StudentSerialzer নামক সিরিয়ালাইজার ক্লাসটি নির্দেশ করে।
এই সিরিয়ালাইজার ক্লাসটি Student মডেলের ডেটাকে JSON বা অন্যান্য ফরম্যাটে রূপান্তর করার কাজ করে।
# authentication_classes = [SessionAuthentication]:

এখানে authentication_classes নামে একটি অপশনাল সেটিং মন্তব্য (comment) আকারে দেওয়া হয়েছে যা SessionAuthentication ব্যবহার করার কথা বলে।
এটি সক্রিয় করা হলে, ভিউসেটটি সেশন বেসড অথেনটিকেশন ব্যবহার করে।
# permission_classes = [IsAuthenticated]:

এখানে permission_classes নামে আরেকটি অপশনাল সেটিং মন্তব্য আকারে দেওয়া হয়েছে যা বলে যে শুধুমাত্র অথেনটিকেটেড (authenticated) ইউজাররা এই ভিউসেটে অ্যাক্সেস পাবে।
এটি সক্রিয় করা হলে, শুধুমাত্র লগ ইন করা ইউজাররাই ভিউসেটের অ্যাক্সেস পাবে।
এই কোডের মন্তব্য করা অংশগুলো (authentication_classes এবং permission_classes) কার্যকর করলে, এই ভিউসেটটি কেবলমাত্র সেশন-ভিত্তিক অথেনটিকেশন এবং লগ ইন করা ইউজারদের জন্য কার্যকর হবে। বর্তমানে, এটি সকলের জন্য উন্মুক্ত।
'''

    

   




       

