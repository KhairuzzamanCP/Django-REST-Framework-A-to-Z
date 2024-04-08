from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerialzer 
from rest_framework import viewsets
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

'''
এই লাইনে একটি ক্লাস StudentViewSet তৈরি হচ্ছে, যা viewsets.ViewSet ক্লাস থেকে উত্তীর্ণ হচ্ছে। এটি Django REST Framework এর একটি পরিবর্তনশীল view এর জন্য একটি টেমপ্লেট।
'''
class StudentViewSet(viewsets.ViewSet):
    serializer_class = StudentSerialzer
    '''
    এই লাইনে একটি ক্লাস StudentViewSet তৈরি হচ্ছে, যা viewsets.ViewSet ক্লাস থেকে উত্তীর্ণ হচ্ছে। এটি Django REST Framework এর একটি পরিবর্তনশীল view এর জন্য একটি টেমপ্লেট।
    '''
    def list(self, request):
        '''
        list মেথডটি GET অনুমোদনের জন্য তথ্য প্রদান করে।
        '''
        print('**********List**********')
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        
        stu = Student.objects.all()
        '''
        Student মডেলের সব অব্জেক্ট নিয়ে আসে।
        '''
        serializer = StudentSerialzer(stu, many = True)
        '''
        StudentSerializer ক্লাস কে ব্যবহার করে stu অব্জেক্ট সিরিয়ালাইজ করে। 'many=True' সমতলের মাধ্যমে একাধিক অব্জেক্ট সিরিয়ালাইজ করা হচ্ছে বলে নির্দেশ করে।
        '''
        return Response(serializer.data)
    '''
    সিরিয়ালাইজার থেকে পাওয়া ডেটা দ্বারা HTTP সার্ভারের প্রতিসাদ হিসাবে প্রদর্শন করা হচ্ছে।
    '''
    def retrieve(self, request, pk=None):
            print('**********Retrieve**********')
            print("Basename:", self.basename)
            print("Action:", self.action)
            print("Detail:", self.detail)
            print("Suffix:", self.suffix)
            print("Name:", self.name)
            print("Description:", self.description)
            id =pk
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerialzer(stu)
                return Response(serializer.data)
    

    '''
    

    নীচে এই ফাংশনের ব্যাখ্যা দেওয়া হল:

    def: এটি পাইথনে একটি ফাংশন ডিফাইন করার জন্য ব্যবহৃত কীওয়ার্ড।

    retrieve: এটি ফাংশনের নাম। এই ফাংশনের কাজ হচ্ছে একটি নির্দিষ্ট স্টুডেন্ট অবজেক্ট রিট্রিভ করা।

    (self, request, pk=None): এই ফাংশনের প্যারামিটার। self ক্লাসের নিজস্ব অবজেক্ট রেফারেন্স নেয়। request হল এইচটিটিটি এমএস (HTTP) অনুরোধ অবজেক্ট, যা ক্লায়েন্ট থেকে প্রাপ্ত হয়। pk হল প্রাইমারি কি (Primary Key) যা স্টুডেন্ট অবজেক্ট আইডেন্টিফাই করে।

    id = pk: এই লাইনে প্রাইমারি কি থেকে আইডেন্টিফাই করা হয়।

    if id is not None:: এই লাইনে প্রাইমারি কি নিজের নাল না হলে নিম্নলিখিত কোড স্থানান্তর করা হয়।

    stu = Student.objects.get(id=id): এই লাইনে ডেটাবেস থেকে স্টুডেন্ট অবজেক্ট রিট্রিভ করা হয় যেটির প্রাইমারি কি সেই id এর সাথে মিলে।

    serializer = StudentSerialzer(stu): এই লাইনে স্টুডেন্ট অবজেক্ট সিরিয়ালাইজ করা হয়।
    '''

    def create(self,request):
        print('**********Create**********')
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)

        serializer = StudentSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg: Data Created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
    '''
    নিচে এই ফাংশনের বিশ্লেষণ দেওয়া হল:
    
    def: এটি পাইথনে একটি ফাংশন ডিফাইন করার জন্য ব্যবহৃত কীওয়ার্ড।

    create: ফাংশনের নাম। এই ফাংশনের কাজ হচ্ছে নতুন স্টুডেন্ট তথ্য তৈরি করা এবং সংরক্ষণ করা।

    (self, request): ফাংশনের প্যারামিটার। self ক্লাসের নিজস্ব অবজেক্ট রেফারেন্স নেয়। request হল এইচটিটিটি এমএস (HTTP) অনুরোধ অবজেক্ট, যা ক্লায়েন্ট থেকে প্রাপ্ত হয়।

    serializer = StudentSerialzer(data=request.data): সিরিয়ালাইজার ইনস্ট্যান্স তৈরি করা হয় এবং এর ডেটা হল ক্লায়েন্ট থেকে প্রাপ্ত ডেটা।

    if serializer.is_valid():: এই লাইনে সিরিয়ালাইজারের ডেটা যদি সঠিক হয়, তাহলে সেটা সংরক্ষন করা হয়।

    serializer.save(): এই লাইনে সিরিয়ালাইজারের ডেটা সংরক্ষন করা হয়।

    return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED): সারিয়ালাইজারের ডেটা সংরক্ষন সফল হলে সাফল্যের মেসেজ রিটার্ন করা হয় এবং হ্যান্ডলারের উত্তর হিসেবে প্রেরণ করা হয়। এখানে status.HTTP_201_CREATED হল সাফল্যের কোড।

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST): সিরিয়ালাইজারের ডেটা সংরক্ষন সফল না হলে এরর মেসেজ রিটার্ন করা হয় এবং এরর কোড রিটার্ন করা হয়। এখানে status.HTTP_400_BAD_REQUEST হল ব্যর্থতার কোড।


    '''
    
    def update(self, request, pk):
        print('**********Update**********')
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerialzer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    '''
    এই কোডটি পাইথন এপিআই ভিউ ক্লাসের একটি মেথডের সাথে সম্পর্কিত। এই মেথডের নাম "update" যা HTTP PUT অনুরোধ পেতে। এই মেথড একটি ছাত্র (Student) অবজেক্ট এর তথ্য আপডেট করে।

    self: এই কোডে ক্লাস মেথড ব্যবহার হচ্ছে এবং সেটা ক্লাস নিজেই রেফারেন্স করছে।
    request: এটি HTTP অনুরোধের বিন্যাস পরিবর্তন করতে ব্যবহৃত হচ্ছে, যা আপডেট করতে হবে।
    pk: এটি প্রাইমারি কি (primary key) যা দিয়ে ছাত্র অবজেক্ট আইডেন্টিফাই করা হয়।
    id = pk: প্রাইমারি কি ক্লাসের প্রোপার্টির মাধ্যমে একটি ভ্যারিয়েবলে স্টোর করা হচ্ছে।
    stu = Student.objects.get(pk=id): এই লাইনে, প্রাইমারি কি ব্যবহার করে স্টুডেন্ট মডেল থেকে স্টুডেন্ট অবজেক্ট পেতে হচ্ছে।
    serializer = StudentSerialzer(stu, data=request.data): এই লাইনে, স্টুডেন্ট মডেল অবজেক্টকে সিরিয়ালাইজ করতে স্টুডেন্টসিরিয়ালাইজার ব্যবহার করা হচ্ছে।
    if serializer.is_valid():: এই শর্তটি পরীক্ষা করে যে, সিরিয়ালাইজার এর তথ্য বৈধ কিনা।
    serializer.save(): যদি তথ্য বৈধ হয়, তবে সিরিয়ালাইজার অবজেক্টের তথ্য সংরক্ষণ করা হচ্ছে।
    return Response({'Complete Data Updated'}, status= status.HTTP_201_CREATED): যদি সম্পূর্ণ তথ্য সফলভাবে আপডেট হয়, তবে HTTP স্ট্যাটাস কোড ২০১ দিয়ে সফল অনুরোধ সংকেত করা হচ্ছে।
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST): যদি তথ্য বৈধ না হয়, তবে ত্রুটি ম্যাসেজ সহ HTTP স্ট্যাটাস কোড ৪০০ দিয়ে অসফল অনুরোধ সংকেত করা হচ্ছে।
    '''
    
    def partial_update(self, request, pk):
        print('*********Partial Update**********')
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerialzer(stu, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    '''
    এই কোডটি পাইথন এপিআই ভিউ ক্লাসের একটি মেথডের সাথে সম্পর্কিত। এই মেথডটি HTTP PATCH অনুরোধের জন্য ব্যবহৃত হয়। এটি একটি ছাত্র (Student) অবজেক্টের তথ্য একাধিকভাবে আপডেট করে।

    self: এই কোডে ক্লাস মেথড ব্যবহার হচ্ছে এবং সেটা ক্লাস নিজেই রেফারেন্স করছে।
    request: এটি HTTP অনুরোধের বিন্যাস পরিবর্তন করতে ব্যবহৃত হচ্ছে, যা আপডেট করতে হবে।
    pk: এটি প্রাইমারি কি (primary key) যা দিয়ে ছাত্র অবজেক্ট আইডেন্টিফাই করা হয়।
    id = pk: প্রাইমারি কি ক্লাসের প্রোপার্টির মাধ্যমে একটি ভ্যারিয়েবলে স্টোর করা হচ্ছে।
    stu = Student.objects.get(pk=id): এই লাইনে, প্রাইমারি কি ব্যবহার করে স্টুডেন্ট মডেল থেকে স্টুডেন্ট অবজেক্ট পেতে হচ্ছে।
    serializer = StudentSerialzer(stu, data=request.data, partial=True): এই লাইনে, স্টুডেন্ট মডেল অবজেক্টকে সিরিয়ালাইজ করতে স্টুডেন্টসিরিয়ালাইজার ব্যবহার করা হচ্ছে। এখানে partial=True সেট করা হয়েছে যাতে পুরো অবজেক্ট না আপডেট করে কিছু ফিল্ড আলাদা আপডেট করা যায়।
    if serializer.is_valid():: এই শর্তটি পরীক্ষা করে যে, সিরিয়ালাইজার এর তথ্য বৈধ কিনা।
    serializer.save(): যদি তথ্য বৈধ হয়, তবে সিরিয়ালাইজার অবজেক্টের তথ্য সংরক্ষণ করা হচ্ছে।
    return Response({'Partial Data Updated'}, status=status.HTTP_201_CREATED): যদি অংশগ্রহণ করে তথ্য সফলভাবে আপডেট হয়, তবে HTTP স্ট্যাটাস কোড ২০১ দিয়ে সফল অনুরোধ সংকেত করা হচ্ছে।
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST): যদি তথ্য বৈধ না হয়, তবে ত্রুটি ম্যাসেজ সহ HTTP স্ট্যাটাস কোড ৪০০ দিয়ে অসফল অনুরোধ সংকেত করা হচ্ছে।
    '''
      
    def destroy(self, request, pk):
        print('**********Destroy**********')
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    
    '''
    
এই কোডটি পাইথন এপিআই ভিউ ক্লাসের একটি মেথডের সাথে সম্পর্কিত। এই মেথডটি HTTP DELETE অনুরোধের জন্য ব্যবহৃত হয়। এটি একটি ছাত্র (Student) অবজেক্টের মুছে ফেলবে।

self: এই কোডে ক্লাস মেথড ব্যবহার হচ্ছে এবং সেটা ক্লাস নিজেই রেফারেন্স করছে।
request: এটি HTTP অনুরোধের বিন্যাস পরিবর্তন করতে ব্যবহৃত হচ্ছে, যা মুছে ফেলতে হবে।
pk: এটি প্রাইমারি কি (primary key) যা দিয়ে ছাত্র অবজেক্ট আইডেন্টিফাই করা হয়।
id = pk: প্রাইমারি কি ক্লাসের প্রোপার্টির মাধ্যমে একটি ভ্যারিয়েবলে স্টোর করা হচ্ছে।
stu = Student.objects.get(pk=id): এই লাইনে, প্রাইমারি কি ব্যবহার করে স্টুডেন্ট মডেল থেকে স্টুডেন্ট অবজেক্ট পেতে হচ্ছে।
stu.delete(): এই লাইনে, স্টুডেন্ট অবজেক্টটি ডিলিট করা হচ্ছে।
return Response({'msg':'Data Deleted'}): মুছে ফেলার পরে সফলভাবে মুছে ফেলা সংকেত দেওয়া হচ্ছে।
    '''

        
    
            
    



   




       

