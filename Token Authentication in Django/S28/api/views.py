from .models import Student
from .serializers import StudentSerialzer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
  
    
'''
এই কোডটি একটি Django REST Framework এর ViewSet ক্লাস ডেফাইন করে। এটি একটি ModelViewSet হিসেবে কাস্টমাইজ করা হয়েছে, অর্থাৎ এটি ডাটা সম্পর্কিত অনেক কাজ করতে পারে, যেমন ডাটা সংগ্রহ, সংশোধন, মুছে ফেলা ইত্যাদি।

queryset প্রপার্টি একটি queryset কে ডিফাইন করে যা স্টুডেন্ট মডেলের সব অবজেক্ট সংগ্রহ করে।

serializer_class প্রপার্টি ডাটা সিরিয়ালাইজ করার জন্য একটি সিরিয়ালাইজার ক্লাস নির্দেশ করে, যা এই মডেলের ডাটা কে জাভাস্ক্রিপ্ট অবজেক্টে রূপান্তরিত করে দেখায়।

authentication_classes প্রপার্টি নির্দেশ করে এই ভিউসেটের জন্য কোন প্রকারের অথেন্টিকেশন ব্যবহার করা হবে, এখানে টোকেন অথেন্টিকেশন ব্যবহৃত হচ্ছে, যা REST অ্যাপ্লিকেশনের জন্য প্রচলিত একটি ধরনের অথেন্টিকেশন মেথড।

permission_classes প্রপার্টি নির্দেশ করে এই ভিউসেটের জন্য কোন ধরনের অনুমতি প্রয়োজন, এখানে IsAuthenticatedOrReadOnly নির্দেশ করে যে এই ডাটা সাধারণত পড়া, লেখা অথবা হালনাগাদ করা যাবে কেবল অকাউন্ট অনুমতি থাকলে।
'''
    

   




       

