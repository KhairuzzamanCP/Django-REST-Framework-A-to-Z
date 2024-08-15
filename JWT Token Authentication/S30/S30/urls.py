"""
URL configuration for S30 project.

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
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView



# Creating Router Object
'''
DefaultRouter হল একটি ব্যবহারিক ক্লাস যা Django REST Framework-এর রাউটিং এবং URL কনফিগারেশন সহজে করে দেয়। এটি ব্যবহার করে আপনি খুব সহজেই RESTful API এর URL পাতা নির্ধারণ করতে পারেন। আপনি এটি ব্যবহার করে URL প্যাটার্ন এবং ভিউ ফাংশনের মাপ করতে পারেন।
TokenObtainPairView:

এই ভিউটি ব্যবহারকারীর লগইন তথ্য (যেমন: username এবং password) যাচাই করে এবং সফল হলে একটি অ্যাক্সেস টোকেন এবং একটি রিফ্রেশ টোকেন প্রদান করে। অ্যাক্সেস টোকেনটি ব্যবহারকারীর পরিচয় যাচাইয়ের জন্য পরবর্তী অনুরোধে ব্যবহার করা হয়, এবং রিফ্রেশ টোকেনটি নতুন অ্যাক্সেস টোকেন জেনারেট করার জন্য ব্যবহৃত হয় যখন আগেরটি এক্সপায়ার হয়ে যায়।
TokenRefreshView:

এই ভিউটি রিফ্রেশ টোকেনের মাধ্যমে নতুন একটি অ্যাক্সেস টোকেন জেনারেট করার জন্য ব্যবহৃত হয়। অর্থাৎ, আপনি যখন একটি রিফ্রেশ টোকেন পাঠাবেন, তখন এই ভিউটি আপনাকে নতুন একটি অ্যাক্সেস টোকেন প্রদান করবে।
TokenVerifyView:

এই ভিউটি একটি প্রদত্ত টোকেন বৈধ কিনা তা যাচাই করার জন্য ব্যবহৃত হয়। আপনি যদি কোনো টোকেন যাচাই করতে চান যে সেটি বৈধ এবং পরিবর্তিত হয়নি, তাহলে এই ভিউটি ব্যবহার করবেন।
এই তিনটি ভিউই JWT ব্যবহারের সময় অত্যন্ত গুরুত্বপূর্ণ এবং নিরাপত্তার জন্য প্রয়োজনীয়।
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
    path('gettoken/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify')
]

'''
এই কোডটির ব্যাখ্যা বাংলায়:

path('admin/', admin.site.urls):

এই লাইনে, 'admin/' URL-টি Django-এর ডিফল্ট অ্যাডমিন ইন্টারফেসের সাথে যুক্ত করা হয়েছে। অর্থাৎ, যদি আপনি আপনার ব্রাউজারে http://yourdomain/admin/ লিখেন, তাহলে Django-এর অ্যাডমিন প্যানেল দেখতে পাবেন।
path('', include(router.urls)):

এই লাইনে, প্রধান URL ('' অর্থাৎ রুট URL) এপ্লিকেশনের বিভিন্ন URL রাউটারের মাধ্যমে অন্তর্ভুক্ত করা হয়েছে। এটি সাধারণত API রাউটিং এর ক্ষেত্রে ব্যবহৃত হয়, যেখানে router.urls-এর মধ্যে সমস্ত এন্ডপয়েন্ট (endpoints) সংজ্ঞায়িত থাকে।
path('gettoken/',TokenObtainPairView.as_view(), name='token_obtain_pair'):

এখানে 'gettoken/' URL-এ TokenObtainPairView ভিউটি যুক্ত করা হয়েছে, যা JWT (JSON Web Token) তৈরির জন্য ব্যবহৃত হয়। এই এন্ডপয়েন্টে আপনার লগইন তথ্য (username এবং password) দিলে একটি অ্যাক্সেস টোকেন এবং একটি রিফ্রেশ টোকেন পাওয়া যাবে।
path('refreshtoken/',TokenRefreshView.as_view(), name='token_refresh'):

'refreshtoken/' URL-টি রিফ্রেশ টোকেনের মাধ্যমে নতুন অ্যাক্সেস টোকেন জেনারেট করার জন্য ব্যবহৃত হয়। যখন আপনার অ্যাক্সেস টোকেন এক্সপায়ার হয়ে যায়, তখন রিফ্রেশ টোকেন ব্যবহার করে নতুন একটি অ্যাক্সেস টোকেন পাওয়া যায়।
path('verifytoken/',TokenVerifyView.as_view(), name='token_verify'):

'verifytoken/' URL-এ TokenVerifyView ভিউ যুক্ত করা হয়েছে, যা কোনো টোকেন বৈধ কিনা তা যাচাই করার জন্য ব্যবহৃত হয়।
'''