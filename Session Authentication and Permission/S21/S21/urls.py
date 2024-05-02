"""
URL configuration for S17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter



# Creating Router Object
'''
DefaultRouter হল একটি ব্যবহারিক ক্লাস যা Django REST Framework-এর রাউটিং এবং URL কনফিগারেশন সহজে করে দেয়। এটি ব্যবহার করে আপনি খুব সহজেই RESTful API এর URL পাতা নির্ধারণ করতে পারেন। আপনি এটি ব্যবহার করে URL প্যাটার্ন এবং ভিউ ফাংশনের মাপ করতে পারেন।
'''
router = DefaultRouter()

# Register StudentViewSet with router

router.register('studentapi', views.StudentModelViewSet, basename='student')
'''
এই কোড লাইনে, আপনি একটি রাউটার ব্যবহার করে স্টুডেন্ট এপিআই (API) এর URL পাতা নির্ধারণ করছেন। এটি অনুসারে, যে বিশেষ এপিআই প্রতিষ্ঠানের ডেটা প্রদর্শন এবং পরিচালনা করা হবে তা নির্ধারণ করার জন্যে StudentViewSet নামক ভিউসেট ক্লাসের ম্যাপিং করা হয়েছে।

router.register ফাংশনের প্যারামিটার হিসেবে নিম্নলিখিত তিনটি প্যারামিটার পাস করা হয়েছে:

'studentapi': এটি হল এপিআই এর পাথ বা URL এর নাম। এটি আপনি এপিআই এর মূল URL এর পরে যুক্ত হবে।
views.StudentModelViewSe: এটি হল ভিউসেট ক্লাস যা আপনি তৈরি করেছেন এবং যেখানে এপিআই এর লজিক এবং প্রদর্শন কোড রয়েছে।
basename='student': এটি হল এপিআই এর নামের বেসেনেম (basename)। এটি পাস করা হয় যাতে এপিআই এর নামের পিছনে যে নামটি থাকবে তা নির্ধারণ করা যায়। এটি একটি ব্যবহারিক প্যারামিটার এবং প্রয়োজন হলে ব্যবহার করা হয়।

*** 
উপরের লাইন কোডটি আপনার এপিআই এর URL পাতা নির্ধারণ করে সেটি যুক্ত করে দেয়। এটি নিজেই URL পাতার সাথে CRUD (Create, Retrieve, Update, Delete) অপারেশন সমন্বয় করে দেয়।
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
