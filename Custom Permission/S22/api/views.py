from .models import Student
from .serializers import StudentSerialzer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
    
    
'''
এই কোডটি একটি Django REST Framework ViewSet দেখাচ্ছে যা একটি `Student` মডেলের জন্য ডিফাইন করা হচ্ছে। এখানে প্রতিটি অংশের কাজ নিম্নে বর্ণিত করা হলো:

- `queryset = Student.objects.all()`: এটি `Student` মডেলের ইন্সট্যান্সগুলি পেতে ব্যবহৃত হবে।

- `serializer_class = StudentSerializer`: এটি সিরিয়ালাইজার ক্লাস নির্দিষ্ট করে, যা `Student` মডেলের ইন্সট্যান্সগুলি সিরিয়ালাইজ এবং ডিসিরিয়ালাইজ করবে।

- `authentication_classes = [SessionAuthentication]`: এটি ইনকামিং অনুরোধগুলি অথেনটিকেট করার জন্য ব্যবহৃত অথেনটিকেশন ক্লাস নির্দিষ্ট করে। এখানে, `SessionAuthentication` ব্যবহৃত হচ্ছে, যা ডিজাঙ্গো সেশন অথেনটিকেশনের উপর ভিত্তি করে।

- `permission_classes`: এটি নির্দিষ্ট করে যে অনুমতি ক্লাসগুলি ব্যবহৃত হবে যেগুলি ইনকামিং অনুরোধটি অনুমোদিত করতে পারবে কিনা।

আপনি `permission_classes` এর অনেকগুলি বিকল্পের মধ্যে কিছু অপশন কমেন্ট করে রেখেছেন এবং একটি অনকমেন্টেড রেখেছেন:

- `permission_classes = [DjangoModelPermissionsOrAnonReadOnly]`: এই পারমিশন ক্লাস অজ্ঞাত ব্যবহারকারীদের (অথবা অন্য কোনও প্রকার প্রাথমিক অনুমতি না থাকা ব্যবহারকারীদের) কে কেবল পড়ার অনুমতি দেয় এবং অথেনটিকেট ব্যবহারকারীদের জন্য ডিজাঙ্গো মডেল অনুমতি ভিত্তিতে অনুমতি প্রদান করে।

আপনার প্রয়োজনীয়তা অনুযায়ী, প্রয়োজনীয় পারমিশন ক্লাসটি চয়ন করতে পারেন যেটি উপলব্ধ অপশনগুলির মধ্যে থাকে বা প্রয়োজন হলে কাস্টম পারমিশন ক্লাস তৈরি করতে পারেন। উদাহরণস্বরূপ, `IsAuthenticated` কেবল অনুমোদিত ব্যবহারকারীদের অ্যাক্সেস দেয়, `IsAdminUser` কেবল অ্যাডমিন ব্যবহারকারীদের অ্যাক্সেস দেয়, এবং এমন অনেক কিছু।
'''


    

   




       

