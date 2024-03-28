# Generic API View and Model Mixin
from .models import Student
from .serializers import StudentSerialzer 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


'''
GenericAPIView: এটি Django REST framework এর অন্যতম জেনেরিক ভিউ ক্লাস যা একটি জেনেরিক এপিআই ভিউ তৈরি করার জন্য ব্যবহৃত হয়। এটি ডেটা প্রসেসিং, ভ্যালিডেশন এবং অন্যান্য HTTP অ্যাপি এর জন্য বিভিন্ন অধিক বিশেষ ফিচার সহজে ব্যবহার করা যায়।

ListModelMixin: এটি Django REST framework এর মিক্সিন (Mixin) ক্লাস, যা লিস্ট ভিউ ফিচার প্রদান করে। এই মিক্সিন ব্যবহার করে আপনি ডাটা লিস্ট রিট্রিভ করতে পারেন (GET request এর মাধ্যমে) এবং নতুন আইটেম সৃষ্টি করতে পারেন (POST request এর মাধ্যমে)।
'''
# List and Create -PK Not Required
class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args,**kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args,**kwargs)
    
# Retrive,Update and Destroy --PK  Required
class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args,**kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args,**kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args,**kwargs)
    


   




       

