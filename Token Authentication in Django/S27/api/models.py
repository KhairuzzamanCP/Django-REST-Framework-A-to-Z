from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
'''
1.মডেলস এবং সেটিংস ইম্পোর্ট:
from django.db import models
from django.conf import settings
এখানে Django এর models এবং settings মডিউলগুলো ইম্পোর্ট করা হয়েছে।

2.Signal এবং Receiver ইম্পোর্ট:

from django.db.models.signals import post_save
from django.dispatch import receiver
এখানে post_save সিগন্যাল এবং receiver ফাংশন ইম্পোর্ট করা হয়েছে যা সিগন্যাল হ্যান্ডেল করার জন্য ব্যবহৃত হয়।

3.Token মডেল ইম্পোর্ট:

from rest_framework.authtoken.models import Token
Django Rest Framework থেকে Token মডেলটি ইম্পোর্ট করা হয়েছে যা টোকেন স্টোর করার জন্য ব্যবহৃত হয়।

4.Receiver ডেকোরেটর ব্যবহার করে সিগন্যাল হ্যান্ডলার তৈরি:

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
এখানে @receiver ডেকোরেটর ব্যবহার করা হয়েছে, যা post_save সিগন্যালের সাথে যুক্ত। যখন settings.AUTH_USER_MODEL (অর্থাৎ, ডিফল্ট ইউজার মডেল) সেভ করা হয়, তখন এই ফাংশনটি চালু হবে।
'''

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length= 100)
    roll = models.IntegerField()
    city = models.CharField(max_length= 100)

# This Singal create Auth Token for Users
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
'''
কোডের ব্যাখ্যা:

@receiver(post_save, sender=settings.AUTH_USER_MODEL):

এটি নির্দেশ করে যে এই ফাংশনটি post_save সিগন্যালের জন্য একটি রিসিভার।
sender=settings.AUTH_USER_MODEL এর মানে এই সিগন্যালটি শুধুমাত্র তখনই ট্রিগার হবে যখন AUTH_USER_MODEL (অর্থাৎ, ইউজার মডেল) সেভ হবে।
**def create_auth_token(sender, instance=None, created=False, kwargs):

এটি সেই ফাংশন যা সিগন্যাল রিসিভ করে।
sender হল সেই মডেল ক্লাস যা সিগন্যাল পাঠিয়েছে।
instance হল সেই মডেলের নির্দিষ্ট ইনস্ট্যান্স যা সেভ হয়েছে।
created একটি বুলিয়ান মান যা নির্দেশ করে যে একটি নতুন রেকর্ড তৈরি হয়েছে কিনা।
**kwargs অতিরিক্ত আর্গুমেন্টগুলি গ্রহণ করে।
if created:

এই শর্তটি চেক করে যে ইউজারটি নতুন তৈরি হয়েছে কিনা।
Token.objects.create(user=instance):

এটি একটি নতুন টোকেন তৈরি করে এবং সেই টোকেনটি সদ্য তৈরি হওয়া ইউজারের সাথে সংযুক্ত করে।
এই পুরো প্রক্রিয়াটি নিশ্চিত করে যে প্রতিবার একটি নতুন ইউজার তৈরি হওয়ার সাথে সাথে স্বয়ংক্রিয়ভাবে একটি প্রমাণীকরণ টোকেন তৈরি হয়, যা API অ্যাক্সেসের জন্য ব্যবহৃত হতে পারে।
'''
