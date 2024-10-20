from rest_framework import serializers
from .models import Song,Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','tittle','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many =True, read_only =True)
    song = serializers.PrimaryKeyRelatedField(many =True, read_only =True)
    song = serializers.HyperlinkedRelatedField(many =True, read_only =True, view_name='song-detail')
    song = serializers.SlugRelatedField(many =True, read_only =True, slug_field='duration')
    song = serializers.HyperlinkedIdentityField(view_name='song-detail')

    class Meta:
        model = Singer
        fields = ['id','name','gender', 'song']
'''
song ফিল্ডের বিভিন্ন ধরন:
python
Copy code
song = serializers.StringRelatedField(many=True, read_only=True)
StringRelatedField: এটি song সম্পর্কিত মডেল (Foreign Key) থেকে __str__() মেথডের আউটপুট প্রদর্শন করে। এখানে many=True মানে একজন Singer-এর একাধিক গান থাকতে পারে এবং read_only=True দিয়ে ইঙ্গিত করা হয়েছে যে এই ফিল্ডে কেবলমাত্র রিড-অনলি (শুধু দেখার) পারমিশন থাকবে, মান পরিবর্তন করা যাবে না।
python
Copy code
song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
PrimaryKeyRelatedField: এটি song সম্পর্কিত মডেল থেকে শুধুমাত্র প্রাইমারি কি (ID) দেখাবে।
python
Copy code
song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
HyperlinkedRelatedField: এটি song ফিল্ডের জন্য URL লিংক তৈরি করে, যা song-detail ভিউ-এর URL-এ যাবে।
python
Copy code
song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='duration')
SlugRelatedField: এটি song মডেলের duration (সময়কাল) ফিল্ডকে ব্যবহার করে ফিল্ডের মান দেখাবে।
python
Copy code
song = serializers.HyperlinkedIdentityField(view_name='song-detail')
HyperlinkedIdentityField: এটি Singer-এর নিজস্ব লিংক তৈরি করবে, যাতে ব্যবহারকারী সরাসরি song-detail ভিউতে যেতে পারে।
2. Meta ক্লাস:
python
Copy code
class Meta:
    model = Singer
    fields = ['id', 'name', 'gender', 'song']
model = Singer:
এখানে Singer মডেলটি সিরিয়ালাইজার হিসেবে ব্যবহার করা হচ্ছে।

fields:
এই লিস্টে যেসব ফিল্ড সিরিয়ালাইজ করা হবে, সেগুলো নির্দিষ্ট করা হয়েছে:

id: Singer-এর ইউনিক আইডি।
name: Singer-এর নাম।
gender: Singer-এর লিঙ্গ।
song: Singer-এর সঙ্গে সম্পর্কিত গানগুলোর তথ্য।
সারসংক্ষেপ:
এই সিরিয়ালাইজার কোডটি Singer মডেলের ডাটা ফরম্যাট করা বা API-তে রিসোর্স হিসেবে পাঠানোর জন্য ব্যবহার করা হচ্ছে। song ফিল্ডের জন্য বিভিন্ন রিলেটেড ফিল্ডের ধরন দেখানো হয়েছে, যেমন প্রাইমারি কি, হাইপারলিঙ্ক, স্ট্রিং, এবং স্লাগ। Meta ক্লাসে নির্দিষ্ট করা হয়েছে কোন মডেল এবং কোন ফিল্ডগুলো সিরিয়ালাইজ করতে হবে।
'''