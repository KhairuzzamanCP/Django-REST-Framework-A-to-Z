from rest_framework.pagination import LimitOffsetPagination

class MyOffsetPagination(LimitOffsetPagination):
   default_limit = 5
   limit_query_param = 'mylimit'
   offset_query_param ='myoffset'
   max_limit = 6
'''
এই কোডটি Django Rest Framework-এর পেজিনেশন সিস্টেম ব্যবহার করে API রেসপন্সে ডেটা লিমিট এবং অফসেট অনুযায়ী ভাগ করে দেখানোর জন্য তৈরি করা হয়েছে।

LimitOffsetPagination ক্লাসটি এক্সটেন্ড (inherit) করে নতুন MyOffsetPagination ক্লাস তৈরি করা হয়েছে।
default_limit = 5: ডিফল্টভাবে একবারে ৫টি আইটেম রিটার্ন করবে।
limit_query_param = 'mylimit': ইউজার চাইলে কাস্টমভাবে mylimit প্যারামিটার দিয়ে লিমিট নির্ধারণ করতে পারবে।
offset_query_param = 'myoffset': myoffset প্যারামিটার দিয়ে ডেটার শুরু পয়েন্ট নির্ধারণ করা যাবে।
max_limit = 6: একবারে সর্বোচ্চ ৬টি ডেটা রিটার্ন করতে পারবে।
'''