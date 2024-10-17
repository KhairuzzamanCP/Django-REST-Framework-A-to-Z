from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 7

'''
MyPageNumberPagination ক্লাসটি Django Rest Framework (DRF)-এ পেজিনেশন পরিচালনার জন্য ব্যবহার করা হচ্ছে। এটি একটি কাস্টম পেজ নম্বর পেজিনেশন ক্লাস, যেখানে ডিফল্ট সেটিংস পরিবর্তন করে ব্যবহারকারীর চাহিদা অনুযায়ী কনফিগার করা হয়েছে। নিচে প্রতিটি সেটিং-এর বাংলা ব্যাখ্যা দেওয়া হলো:

page_size = 4

প্রতি পেজে সর্বোচ্চ ৪টি রেকর্ড দেখাবে।
page_query_param = 'p'

URL-এ p প্যারামিটারের মাধ্যমে পেজ নম্বর নির্ধারণ করা যাবে। উদাহরণ: example.com/api/items?p=2
page_size_query_param = 'records'

ব্যবহারকারী চাইলে URL-এ records প্যারামিটার দিয়ে প্রতি পেজে কতগুলো রেকর্ড দেখাতে চায়, সেটি নির্ধারণ করতে পারবে। উদাহরণ: example.com/api/items?p=1&records=5
max_page_size = 7

এক পেজে সর্বাধিক ৭টি রেকর্ড দেখানো যাবে, এর বেশি দেখানো যাবে না।
এই পেজিনেশন ক্লাসটি API-এর জন্য খুব উপযোগী, কারণ এটি ব্যবহারকারীদের পেজ এবং রেকর্ড সংখ্যা নিয়ন্ত্রণের সুযোগ দেয় এবং API রিসোর্স ব্যবহারে কার্যকরী সীমা আরোপ করে।
'''