from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

"""
এই কোডটি Django Rest Framework (DRF) এ একটি কাস্টম অথেনটিকেশন ক্লাস তৈরি করে। চলুন এই কোডটির প্রতিটি অংশ বাংলায় ব্যাখ্যা করি।

ইমপোর্ট:

BaseAuthentication: এটি Django Rest Framework এর একটি ক্লাস, যা কাস্টম অথেনটিকেশন ক্লাস তৈরি করতে ব্যবহৃত হয়।
AuthenticationFailed: এটি একটি এক্সেপশন, যা অথেনটিকেশন ব্যর্থ হলে রেইজ করা হয়।
User: এটি Django এর ডিফল্ট ইউজার মডেল, যেখানে ইউজার সম্পর্কিত সব তথ্য থাকে।

"""
class CustomAuthentication(BaseAuthentication):
    """
 ক্লাস ডিফিনিশন:

CustomAuthentication: এটি একটি কাস্টম অথেনটিকেশন ক্লাস, যা BaseAuthentication থেকে ইনহেরিট করে তৈরি করা হয়েছে।
    """
    def authenticate(self, request):
        '''
    authenticate মেথড:

    authenticate: এটি একটি মেথড, যা অথেনটিকেশন প্রক্রিয়া সম্পন্ন করার জন্য ব্যবহৃত হয়। এই মেথডটি request প্যারামিটার গ্রহণ করে, যা একটি HTTP রিকোয়েস্ট।
        '''
        username = request.GET.get('username')
        '''
        ইউজারনেম পাওয়া:

        এখানে রিকোয়েস্টের GET প্যারামিটার থেকে username কে নেয়া হয়েছে। অর্থাৎ, রিকোয়েস্টের URL এ username প্যারামিটার থাকতে হবে।
        '''
        if username is None:
            return None
        '''
        ইউজারনেম চেক:

        যদি username না থাকে, তাহলে None রিটার্ন করা হবে। এর মানে হলো, এই অথেনটিকেশন প্রক্রিয়া আর এগোবে না।
        '''
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No Such User')
        return(user, None)
    '''
        try:
            user = User.objects.get(username=username)
            ইউজার খোঁজা:

        User মডেল থেকে username এর উপর ভিত্তি করে ইউজার খোঁজা হচ্ছে। যদি ইউজার পাওয়া যায়, তাহলে user ভেরিয়েবলে সেই ইউজারের অবজেক্ট রাখা হবে।

         except User.DoesNotExist:
            raise AuthenticationFailed('No Such User')

            যদি ইউজার না পাওয়া যায়, তাহলে AuthenticationFailed এক্সেপশন রেইজ করা হবে এবং "No Such User" মেসেজ দেখানো হবে।

                return(user, None)
                যদি ইউজার পাওয়া যায়, তাহলে ইউজারের অবজেক্ট user রিটার্ন করা হবে। দ্বিতীয় প্যারামিটারটি None রাখা হয়েছে, কারণ DRF এর জন্য এটি প্রয়োজনীয়।

    '''


        
         
       
       