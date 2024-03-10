from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
# Create your views here.
'''
api_view ডেকোরেটর:

এটি ফাংশন ভিউগুলি তৈরি করতে ব্যবহৃত হয়।
এটি একটি ভিউ ফাংশনকে API ভিউ হিসেবে চিহ্নিত করে, তাতে Django REST framework এর প্রতিরূপ কাজ করতে সাহায্য করে।
এটি বিভিন্ন HTTP মেথড (GET, POST, PUT, DELETE ইত্যাদি) এর জন্য আপনার কোডের অংশগুলি বুঝাতে সাহায্য করে।
একটি উদাহরণ:

'''
# @api_view()
# def hellow_world(request):
#     return Response({'msg': 'Hello World'})

# @api_view(['GET'])
# def hellow_world(request):
#     return Response({'msg': 'Hello World'})

# @api_view(['POST'])
# def hellow_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg': 'This is post request'})


@api_view(['GET','POST'])
def hellow_world(request):
    if request.method == 'GET':
        return Response({'msg':'This is GET Request'})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'This is POST Request', 'data': request.data})