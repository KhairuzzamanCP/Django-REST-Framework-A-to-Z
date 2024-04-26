from .models import Student
from .serializers import StudentSerialzer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]

'''
এই কোডটি একটি Django REST Framework viewset ক্লাস দেখাচ্ছে, যা স্টুডেন্ট মডেলের তথ্য সম্পর্কে অ্যাক্সেস করতে ব্যবহৃত হয়। এখানে কিছু গুরুত্বপূর্ণ বৈশিষ্ট্য আছে:

`class StudentModelViewSet(viewsets.ModelViewSet):`: এটি একটি Django REST framework এর `ModelViewSet` ক্লাস থেকে একটি সাবক্লাস। এটি Django মডেল অবজেক্ট সম্পর্কিত সমস্ত CRUD (সৃষ্টি, পড়া, আপডেট এবং মুছে ফেলা) অপারেশন সহায়ক করে।

queryset: এটি স্টুডেন্ট মডেল থেকে সব তথ্য নির্বাচন করে।
serializer_class: এটি ব্যবহৃত সিরিয়ালাইজার ক্লাস নির্দেশ করে, যা স্টুডেন্ট মডেলের তথ্য সিরিয়ালাইজ করে রিস্পন্স তৈরি করে।
authentication_classes: এটি ব্যবহার করা হয় প্রাথমিক প্রমাণীকরণের জন্য। এখানে BasicAuthentication ব্যবহৃত হয়েছে, যা বেসিক অ্যাথেন্টিকেশন প্রদান করে।
permission_classes: এটি ব্যবহার করা হয় প্রবেশ নিয়ন্ত্রণের জন্য। এটি ব্যবহৃত হয়েছে তিনটি পারমিশন ক্লাসের জন্য - IsAuthenticated, AllowAny, এবং IsAdminUser। এই নির্দিষ্ট পারমিশনগুলি নির্ধারণ করে যে ব্যবহারকারীরা কোন ধরনের অ্যাক্সেস পেতে পারেন। উদাহরণস্বরূপ, IsAuthenticated ব্যবহৃত হয় একটি অ্যাক্সেস সিদ্ধান্ত করার জন্য যে ব্যবহারকারী প্রমাণীকরণ করে এবং IsAdminUser ব্যবহৃত হয় যারা এডমিনিস্ট্রেটর পর্যালোচনা করেন। AllowAny ব্যবহৃত হয় যে কেউই অ্যাক্সেস করতে পারেন বিনা কোন অবরোধের। এই পারমিশনগুলি নির্ধারণ করে বিভিন্ন প্রকারের ব্যবহারকারীদের সাথে কোন প্রকারের অ্যাক্সেস অনুমতি দেওয়া হচ্ছে।
'''
    

   




       

