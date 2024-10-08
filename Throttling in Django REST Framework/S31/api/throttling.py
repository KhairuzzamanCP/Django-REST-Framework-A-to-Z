from rest_framework.throttling import UserRateThrottle

class JackRateTHrottle(UserRateThrottle):
    scope = 'jack'

'''
UserRateThrottle থেকে ইনহেরিট করা:

JackRateTHrottle ক্লাসটি UserRateThrottle ক্লাস থেকে ইনহেরিট করা হয়েছে। অর্থাৎ, এটি মূলত UserRateThrottle-এর মতো কাজ করবে, যা প্রতিটি অথেনটিকেটেড ইউজারের জন্য নির্দিষ্ট সংখ্যক API রিকোয়েস্টের হার নির্ধারণ করে।
scope = 'jack':

এখানে scope = 'jack' সেট করা হয়েছে। scope এর মান নির্ধারণ করে যে কেমন থ্রটলিং রেট লিমিট ব্যবহার করা হবে। এটি settings.py ফাইলে REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] ডিকশনারিতে একটি কী হিসেবে সংজ্ঞায়িত থাকতে হবে।
'''