from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data  = request.body
        stream = io.BytesIO(json_data)
        ''''
        io: এটি একটি পাইথন মডিউল, যা I/O (ইনপুট/আউটপুট) সম্পর্কিত কাজগুলি সহজ করে তোলে।

        io.BytesIO: এটি একটি BytesIO ক্লাস, যা io মডিউলের একটি উপ-ক্লাস হিসেবে কাজ করে এবং বাইনারি ডেটা সংরক্ষণ করতে সাহায্য করে।

        stream = io.BytesIO(json_data): এই লাইনে, json_data হলো পূর্বে ডেটা স্ট্রিঙ হিসেবে প্রাপ্ত একটি JSON ডেটা। এই ডেটাকে একটি BytesIO অবজেক্টে রূপান্তর করা হয়, যা এখন একটি ইন-মেমোরি বাইনারি স্ট্রিম।
        '''
        pythondata = JSONParser().parse(stream)
        '''
        JSONParser().parse(stream): এই লাইনে, JSONParser ক্লাস ব্যবহার করা হয়েছে এবং এটি ডেটা পার্স করছে যা stream থেকে প্রাপ্ত হয়েছে। এটি রিটার্ন করে একটি পাইথন ডাটা স্ট্রাঙ্গ, যা এখন ভ্যারিয়েবল python_data তে সংরক্ষণ করা হয়েছে।
        '''
        serializer = StudentSerializer( data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse (json_data, content_type ='application/json')
        
        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse (json_data, content_type ='application/json')