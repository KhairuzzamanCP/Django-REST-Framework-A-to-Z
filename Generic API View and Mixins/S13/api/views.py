# Generic API View and Model Mixin
from .models import Student
from .serializers import StudentSerialzer 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


'''
GenericAPIView: এটি Django REST framework এর অন্যতম জেনেরিক ভিউ ক্লাস যা একটি জেনেরিক এপিআই ভিউ তৈরি করার জন্য ব্যবহৃত হয়। এটি ডেটা প্রসেসিং, ভ্যালিডেশন এবং অন্যান্য HTTP অ্যাপি এর জন্য বিভিন্ন অধিক বিশেষ ফিচার সহজে ব্যবহার করা যায়।

ListModelMixin: এটি Django REST framework এর মিক্সিন (Mixin) ক্লাস, যা লিস্ট ভিউ ফিচার প্রদান করে। এই মিক্সিন ব্যবহার করে আপনি ডাটা লিস্ট রিট্রিভ করতে পারেন (GET request এর মাধ্যমে) এবং নতুন আইটেম সৃষ্টি করতে পারেন (POST request এর মাধ্যমে)।
'''
class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args,**kwargs)
    
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args,**kwargs)
    
class StudentRetrive(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args,**kwargs)
    
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args,**kwargs)
    
class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args,**kwargs)
    


   



# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Student
# from .serializers import StudentSerialzer
# from rest_framework import status
# from rest_framework.views import APIView

# # Create your views here.
# '''
#    def get(self, request, pk = None, format = None):
   
#    এই কোডটি একটি ফাংশন ভিউ ক্লাসের মেথড ডেফিনিশন প্রদর্শন করে, যা একটি HTTP GET অনুরোধের জন্য প্রস্তুতি করে। এই মেথডের প্যারামিটার হিসেবে নিম্নলিখিত প্যারামিটারগুলি রয়েছে:

#    self: এটি পাইথনের সেলফ অবজেক্ট, যা অবশ্যই মেথডের প্রথম প্যারামিটার হতে হবে।
#    request: এটি HTTP অনুরোধের সম্পর্কিত তথ্য নিয়ে আসে, যেমন পারামিটার, হেডার, বডি ইত্যাদি।
#    pk: এটি একটি প্রাইমারি কী (অথবা "প্রাইমারি কে" নির্দেশ করে) যা ব্যবহৃত হয় পরিমাণ সংখ্যার ডেটা নির্দেশ করতে হয়। এই মেথড বিশেষভাবে একটি নির্দিষ্ট এন্টিটির (যেমন একটি ডেটাবেস রেকর্ড) ডেটা প্রাপ্ত করতে ব্যবহৃত হয়। এটি একটি অপশনাল প্যারামিটার, এটি প্রয়োজনে বা অপ্সনাল হতে পারে।
#    format: এটি অনুরোধের ফরম্যাট নির্দেশ করে, যেমন JSON, XML ইত্যাদি। এটি অপশনাল প্যারামিটার।
# '''

# class StudentAPI(APIView):
#    def get(self, request, pk=None, format=None):
#       id = pk
#       if id is not None:
#          stu = Student.objects.get(id=id)
#          serializer = StudentSerialzer(stu)
#          return Response(serializer.data)
#       stu = Student.objects.all()
#       serializer = StudentSerialzer(stu, many = True)
#       return Response(serializer.data)
   
#    def post(self,request,format=None):
#       serializer = StudentSerialzer(data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response({'msg':'Data Created'}, status= status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#    def put(self, request,pk=None,format=None):
#       id = pk
#       stu = Student.objects.get(pk=id)
#       serializer = StudentSerialzer(stu, data= request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response({'msg': 'data Updated'})
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#    def patch(self,request,pk=None,format=None):
#       id = pk
#       stu = Student.objects.get(pk=id)
#       serializer = StudentSerialzer(stu, data= request.data, partial = True)
#       if serializer.is_valid():
#           serializer.save()
#           return Response({'msg':'Partial data Updated'})
#       return Response(serializer.errors)
      
   
#    def delete(self, request,pk=None,format=None):
#       id = pk
#       stu = Student.objects.get(pk=id) 
#       stu.delete()
#       return Response({'msg': 'data Deleted'})

       

