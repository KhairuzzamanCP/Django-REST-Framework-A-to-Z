from rest_framework import serializers
from .models import Student


class StudentSeralizer(serializers.ModelSerializer):
    '''
    read_only=True: এটি হলো একটি বৈশিষ্ট্য যা স্ট্রিং ক্ষেত্রটি শুধুমাত্র পড়তে অনুমতি দেয়। 
    '''
    name = serializers.CharField(read_only =True)
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        '''
        read_only_fields = ['name','roll']

        এই লাইনটি সিরিয়ালাইজার ক্লাসে একটি প্রপার্টি হিসেবে একটি লিস্ট নির্দিষ্ট করে, যা ধরে নেয় যে কোনও অবজেক্ট সিরিয়ালাইজ করার সময়, এই ক্লাসের এই লিস্টে উল্লেখিত ক্ষেত্রগুলি শুধুমাত্র পড়ার জন্য হবে, মানে এই ক্ষেত্রগুলি মাধ্যমে ডেটা আপডেট করা হতে পারবে না।
        '''
        # read_only_fields = ['name','roll']
        extra_kwargs = {'name':{'read_only':True}}


