from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    number = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

   
    def create(self, validated_data):
        '''
        def create(self, validated_data):: এই লাইনে create হলো একটি মেথড নাম, যা এই সিরিয়ালাইজার ক্লাসের একটি মেথড। এই মেথডটি নতুন অবজেক্ট তৈরি করতে ব্যবহৃত হয়।

        validated_data: এটি একটি ভ্যালিডেট হওয়া ডেটা অবজেক্ট, যা এই মেথডের প্যারামিটার হিসেবে পাওয়া যায়। এটি সিরিয়ালাইজ করা ডেটা থেকে যা ভ্যালিডেট করা হয়েছে।
        '''
        return Student.objects.create(**validated_data)
        '''
        return Student.objects.create(**validated_data): এই লাইনে, Student.objects.create() হলো একটি ডাটাবেসে নতুন অবজেক্ট তৈরির জন্য ব্যবহৃত মেথড, যেখানে **validated_data একটি ডিকশনারি থাকবে, এবং এই ডিকশনারির কী-ভ্যালু গুলি মডেলের ফিল্ড গুলির সাথে মিলে নতুন অবজেক্ট তৈরি হবে।
        '''
    #   এই মেথডের মূল উদ্দেশ্য হলো নতুন ডেটা ভেরিফাই করার পরে তা মডেলে সংরক্ষণ করা।
        