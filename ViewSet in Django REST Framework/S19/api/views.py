from .models import Student
from .serializers import StudentSerialzer
from rest_framework import viewsets


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer

'''
class StudentModelViewSet(viewsets.ModelViewSet):: এটি একটি Django REST framework এর ModelViewSet ক্লাস থেকে একটি সাবক্লাস। এটি Django মডেল অবজেক্ট সম্পর্কিত সমস্ত CRUD (সৃষ্টি, পড়া, আপডেট এবং মুছে ফেলা) অপারেশন সহায়ক করে।

queryset = Student.objects.all(): এটি মডেল ভিউসেটের জন্য ডিফল্ট ডেটা সেট সেট করে। এখানে Student মডেলের সমস্ত অবজেক্ট নিয়ে আসা হচ্ছে।

serializer_class = StudentSerialzer: এটি মডেল ভিউসেটের জন্য সিরিয়ালাইজার ক্লাস সেট করে। এটি মডেল অবজেক্টগুলি সিরিয়ালাইজ করে এবং সিরিয়ালাইজড অবজেক্টগুলি মডেলের অবজেক্টে পরিণত করে। এখানে StudentSerialzer হলো একটি Django REST framework সিরিয়ালাইজার ক্লাস, যা Student মডেলের সিরিয়ালাইজেশন নিয়ে কাজ করে।
'''
    
   

#

   




       

