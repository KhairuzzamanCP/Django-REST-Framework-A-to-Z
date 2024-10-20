"""
URL configuration for S41 project.

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
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('singer',views.SingerViewset, basename= 'singer'),
router.register('song',views.SongViewset, basename= 'song')

'''
 Router তৈরি করা:
python
Copy code
router = DefaultRouter()
DefaultRouter:
এটি Django Rest Framework এর একটি বিল্ট-ইন রাউটার, যা অটোমেটিকভাবে API এর URL পাথ এবং এন্ডপয়েন্ট তৈরি করে। এর মাধ্যমে ViewSet-গুলো সহজে রাউটের সাথে সংযুক্ত করা যায়।
2. Router-এর সাথে ViewSet রেজিস্টার করা:
python
Copy code
router.register('singer', views.SingerViewset, basename='singer')
router.register('song', views.SongViewset, basename='song')
router.register():

'singer': এই এন্ডপয়েন্টের জন্য URL পাথ হবে /singer/।
views.SingerViewset:
SingerViewset হলো একটি ViewSet, যেটি Singer সম্পর্কিত CRUD অপারেশন (create, read, update, delete) হ্যান্ডল করবে।
basename='singer':
basename রাউটারের জন্য একটি আলাদা নাম তৈরি করে, যা SingerViewSet থেকে আসা URL গুলো আলাদা করতে সহায়তা করে।
একইভাবে,

'song': এর URL পাথ হবে /song/।
SongViewset মডেলের গান সংক্রান্ত API গুলো পরিচালনা করবে।
3. Router কীভাবে কাজ করে?
এই রাউটার কোডের ফলে নিম্নলিখিত API এন্ডপয়েন্টগুলো অটোমেটিক্যালি তৈরি হবে:

/singer/ – Singer-এর লিস্ট এবং নতুন Singer তৈরি।
/singer/{id}/ – নির্দিষ্ট Singer এর বিস্তারিত দেখা, আপডেট বা ডিলিট করা।
/song/ – Song-এর লিস্ট এবং নতুন Song তৈরি।
/song/{id}/ – নির্দিষ্ট Song এর বিস্তারিত দেখা, আপডেট বা ডিলিট করা।
সারসংক্ষেপ:
এই Router কোডটি Singer এবং Song এর জন্য API রাউটিং সেটআপ করে, যাতে আমরা ViewSet ব্যবহার করে RESTful API তৈরি করতে পারি। DefaultRouter রাউটারের মাধ্যমে URL পাথ এবং এন্ডপয়েন্টগুলো সহজে ম্যানেজ করা যায়।
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace= 'rest_framework')),
   

]
