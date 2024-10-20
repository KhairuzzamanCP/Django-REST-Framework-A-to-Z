from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
'''
class Singer(models.Model):
Singer হলো একটি মডেল যা ডাটাবেসে একটি টেবিল তৈরি করবে।
models.Model হলো Django-এর বিল্ট-ইন ক্লাস, যা প্রত্যেক মডেলের জন্য বেস (base) হিসেবে কাজ করে।
2. name = models.CharField(max_length=100)
name হলো একটি ফিল্ড, যেখানে গায়কের নাম রাখা হবে।
models.CharField একটি ডাটাটাইপ যা স্ট্রিং (টেক্সট) ডেটা রাখে।
max_length=100 মানে সর্বোচ্চ ১০০ অক্ষর পর্যন্ত নাম রাখা যাবে।
3. gender = models.CharField(max_length=100)
gender ফিল্ডে গায়কের লিঙ্গের তথ্য রাখা হবে (যেমন: Male, Female)।
max_length=100 মানে সর্বোচ্চ ১০০ অক্ষর পর্যন্ত টেক্সট এখানে রাখা যাবে।
4. def __str__(self):
এই মেথডটি মডেলের প্রতিটি অবজেক্টের জন্য একটি রিডেবল রূপ (representational string) তৈরি করে।
এখানে return self.name মানে হলো, যখনই আমরা কোনো Singer অবজেক্ট প্রিন্ট করব বা দেখতে চাইব, তখন গায়কের নাম প্রদর্শিত হবে।
সংক্ষেপে:
এই মডেলটি Django ডাটাবেসে গায়কদের নাম ও লিঙ্গ সংরক্ষণ করতে ব্যবহৃত হবে। যখন এই মডেলের কোনো অবজেক্ট দেখা হবে, তখন শুধু গায়কের নাম দেখাবে।
'''

class Song(models.Model):
    tittle = models.CharField(max_length=50)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    duration = models.IntegerField()

    def __str__(self):
        return self.tittle
    
'''
1. class Song(models.Model):
Song হলো একটি Django মডেল, যা ডাটাবেসে একটি টেবিল তৈরি করবে, যেখানে গানের তথ্য রাখা হবে।
models.Model হলো Django-এর বেস ক্লাস, যা সব মডেলের জন্য ভিত্তি হিসেবে কাজ করে।
2. tittle = models.CharField(max_length=50)
tittle ফিল্ডে গানের শিরোনাম (title) সংরক্ষিত হবে।
models.CharField হলো একটি টেক্সট ডেটা ফিল্ড, যা সর্বোচ্চ ৫০টি অক্ষর পর্যন্ত ডেটা রাখবে।
(বিঃদ্রঃ) এখানে tittle বানানে ভুল রয়েছে, এটি title হওয়া উচিত।
3. singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
singer হলো একটি ForeignKey, যা Song এবং Singer মডেলের মধ্যে সম্পর্ক স্থাপন করে।
ForeignKey ব্যবহার করে একাধিক গানকে (Song) একজন গায়কের (Singer) সঙ্গে যুক্ত করা যায়।
on_delete=models.CASCADE: যদি কোনো গায়ক (Singer) ডিলিট করা হয়, তাহলে তার সাথে যুক্ত সব গানও ডিলিট হয়ে যাবে।
related_name='song': এর মাধ্যমে আমরা Singer মডেল থেকে songs (গানগুলো) রিলেট করতে পারব। উদাহরণ: singer.song.all()।
4. duration = models.IntegerField()
duration ফিল্ডে গানের মেয়াদ বা দৈর্ঘ্য (সেকেন্ডে) সংরক্ষিত হবে।
models.IntegerField ব্যবহার করে পূর্ণসংখ্যা (integer) আকারে ডেটা রাখা হয়।
5. def __str__(self):
এই মেথডটি মডেলের প্রতিটি অবজেক্টকে রিডেবল ফরম্যাটে রিটার্ন করে।
return self.tittle: যখন আমরা কোনো Song অবজেক্ট প্রিন্ট করব, তখন গানের শিরোনাম (title) দেখাবে।
সংক্ষেপে:
এই Song মডেলটি গানের শিরোনাম, গায়কের রেফারেন্স এবং গানের দৈর্ঘ্য সংরক্ষণ করতে ব্যবহৃত হবে। এটি Singer মডেলের সাথে সম্পর্কিত, এবং যখন গায়ক ডিলিট করা হবে, তখন তার গানগুলোও ডিলিট হয়ে যাবে।
'''