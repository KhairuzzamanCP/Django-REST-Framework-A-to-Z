from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False
'''
এই কোডে, MyPermission ক্লাসটি BasePermission ক্লাস থেকে প্রসারিত করা হয়েছে। এটি একটি অনুমতি ক্লাস যা Django REST Framework এর মধ্যে ব্যবহৃত হয়।

has_permission মেথডটি অনুমতি পরীক্ষা করে এবং এটি ফেরত দেয়। এখানে আমরা চেক করছি কোন মেথডে রিকোয়েস্ট আসে তার। যদি রিকোয়েস্ট 'POST' মেথড হয়, তবে আমরা ট্রু (True) ফেরত দেব। অন্যথায়, আমরা ফলাফলে ফল্স (False) ফেরত দেব।

এই পারমিশন এখন যদি কোন রিকোয়েস্ট 'POST' মেথডের হয়, তাহলে অনুমতি দেবে। অন্যথায়, অনুমতি দেওয়া হবে না।
'''