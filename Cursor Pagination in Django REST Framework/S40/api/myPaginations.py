from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
  page_size = 5
  ordering = 'name'

'''
CursorPagination:
এটি এমন একটি pagination পদ্ধতি, যেখানে পরবর্তী পৃষ্ঠার ডেটা লোড করার জন্য cursor ব্যবহার করা হয়। Cursor মানে হলো এমন একটি পয়েন্ট, যা আগে কোথায় শেষ হয়েছিল তা মনে রাখে।

page_size = 5:
একবারে সর্বোচ্চ ৫টি রেকর্ড দেখাবে। অর্থাৎ, response-এ এক পেজে শুধু ৫টি ডেটা পাঠাবে।

ordering = 'name':
ডেটাগুলোকে name ফিল্ড অনুসারে সাজানো হবে (অক্ষর ক্রমানুসারে)। অর্থাৎ, নাম ধরে ascending order-এ রেকর্ডগুলো দেখা যাবে।

Cursor Pagination কবে ব্যবহার করা ভালো?
যখন তোমার ডেটাসেট বড় এবং দ্রুত response দরকার।
Offset-based pagination (যেমন page number) এর তুলনায় এটি বেশি efficient, কারণ প্রতিবার পুরোনো পজিশন মনে রাখার দরকার হয় না।
এটি API-তে performance বাড়াতে সাহায্য করে, বিশেষত যখন অনেক ডেটা নিয়ে কাজ করতে হয়।

'''