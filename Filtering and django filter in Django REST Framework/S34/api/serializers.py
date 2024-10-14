
from rest_framework import serializers
from .models import Student

class StudentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city','passby']

'''
from rest_framework import serializers
এখানে Django Rest Framework (DRF) থেকে serializers ইমপোর্ট করা হয়েছে, যা ডেটা কনভার্সনের জন্য ব্যবহৃত হয় (যেমন: Python Objects থেকে JSON-এ রূপান্তর)।
২. from .models import Student
models.py ফাইল থেকে Student মডেলটি ইমপোর্ট করা হয়েছে। এই মডেলটিতে শিক্ষার্থীদের তথ্য (যেমন: name, roll, city ইত্যাদি) সংরক্ষিত থাকে।
৩. class StudentSerializer(serializers.ModelSerializer):
আমরা StudentSerializer নামের একটি serializer তৈরি করছি, যা serializers.ModelSerializer থেকে ইনহেরিট করেছে। এটি Student মডেলের উপর ভিত্তি করে ডেটা সিরিয়ালাইজ ও ডি-সিরিয়ালাইজ করবে।
(সিরিয়ালাইজ মানে হলো মডেলের ডেটা JSON বা অন্যান্য ফরম্যাটে রূপান্তর করা।)
৪. class Meta:
Meta ক্লাস ব্যবহার করে মডেল সম্পর্কিত অতিরিক্ত কনফিগারেশন করা হয়।
৫. model = Student
এখানে বলা হয়েছে যে এই serializer টি Student মডেলের উপর কাজ করবে।
৬. fields = ['id', 'name', 'roll', 'city', 'passby']
এই লাইনটি নির্দেশ করে কোন কোন field সিরিয়ালাইজ করা হবে। এখানে Student মডেলের id, name, roll, city এবং passby ফিল্ডগুলোকে আমরা অন্তর্ভুক্ত করেছি।
সারমর্ম:
এই serializer-টি Student মডেলের তথ্যকে JSON ফরম্যাটে রূপান্তর করতে সাহায্য করবে। এটি REST API এর মাধ্যমে ডেটা পাঠানো বা গ্রহণ করার সময় ব্যবহার করা হয়।
'''