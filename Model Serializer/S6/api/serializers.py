from rest_framework import serializers
from .models import Student


class StudentSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

# class StudentSeralizer(serializers.Serializer):
#     name = serializers.CharField(max_length = 100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length = 100)


#     '''
#     create হলো এই মেথডের নাম, এটি একটি নতুন মডেল ইনস্ট্যান্স তৈরি করতে ব্যবহৃত হয়।
#     self এটি একটি ক্লাস মেথড, এটি ক্লাস নিজেই মেথডটি ব্যবহার করতে পারে।
#     validated_data এটি একটি ডিকশনারি, এটি একটি ইনকামিং ডেটা হিসেবে প্রদান হয় এবং এই ডেটা একটি ভ্যালিডেটেড সিরিয়ালাইজড ডাটা।
#     Student.objects.create(**validated_data) এটি একটি মডেল ম্যানেজার মেথড, এটি একটি নতুন মডেল ইনস্ট্যান্স তৈরি করে এবং সেই ইনস্ট্যান্সে ডাটা সেট করে যা validated_data থেকে আসে।
#     **validated_data এটি একটি ডাটা কর্মফল হলে যা সিরিয়ালাইজ হয়ে থাকে, সেই ডাটা কেউ মডেল ইনস্ট্যান্সে সেট করতে একটি উপায়।
#     এই কোডে, একটি নতুন মডেল ইনস্ট্যান্স তৈরি করা হয় Student মডেলের সাথে এবং সেই ইনস্ট্যান্সে validated_data থেকে আসা ডাটা সেট করা হয়।
#     '''
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#     '''
#     create: এটি মেথডের নাম, এই মেথডের মাধ্যমে নতুন ইনস্ট্যান্স তৈরি হয়।

#     self: এটি একটি ক্লাস মেথড, এটি ক্লাস নিজেই মেথডটি ব্যবহার করতে পারে।

#     validated_data: এটি একটি ডিকশনারি, এটি সিরিয়ালাইজার দ্বারা ভ্যালিডেট এবং ডিসিরিয়ালাইজ করা হয় ডাটা ধারণ করে।

#     Student.objects.create(**validated_data): এটি একটি মডেল ম্যানেজার মেথড, এটি একটি নতুন মডেল ইনস্ট্যান্স তৈরি করে এবং সেই ইনস্ট্যান্সে ডাটা সেট করে যা validated_data থেকে আসে।

#     **validated_data: এটি ডাটা কর্মফল হলে, সেই ডাটা কে মডেল ইনস্ট্যান্সে সেট করতে একটি উপায়, ডাটা একেবারে সিরিয়ালাইজ হয়ে থাকে এবং মডেল ফিল্ডের সাথে যোগাযোগ করতে এটি অব্যহৃত হয়।

#     সারাংশঃ এই কোডটি ভ্যালিডেটেড ডাটা নেয় এবং একটি নতুন Student মডেল ইনস্ট্যান্স তৈরি করে যা সেই ডাটা দিয়ে সেট করে।
    
#     '''
#     def update(self, instance, validated_data):
#         '''
#         এই লাইন দ্বারা বুঝাচ্ছে আপডেট হওয়ার আগের ডাটা
#         '''
#         print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         '''
#         এই লাইন দ্বারা বুঝাচ্ছে আপডেট হওয়ার পর ডাটা
#         '''
#         print(instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         print(instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         print(instance.city)
#         instance.save()
#         return instance
