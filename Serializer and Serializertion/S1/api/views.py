from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse


# Model objects singel student data
def student_detial(request,pk):
    '''
    stu = Student.objects.get(id = pk) mane:
    one id  student  data deka jabe
    '''
    stu = Student.objects.get(id = pk)
    # print('stu', stu)
    serialzer = StudentSerializer(stu)
    # print('serialzer', serialzer)
    # print('serialzer data', serialzer.data)
    json_data = JSONRenderer().render(serialzer.data)
    # print('json_data', json_data)
    return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serialzer.data)

# Ouery Set - All Student Data
def student_list(request):
    '''
    stu = Student.objects.all(mane:
    sob student id data deka jabe
    '''
    stu = Student.objects.all()
    # print('stu', stu)
    '''
    serialzer = StudentSerializer(stu, many=True): এখানে "StudentSerializer" নামক সিরিয়ালাইজার ইনস্ট্যান্ট তৈরি হচ্ছে, এবং এটি "stu" অবজেক্টগুলি সিরিয়ালাইজ করতে ব্যবহৃত হচ্ছে। many=True এটি বুঝায় যে, এটি একাধিক অবজেক্টের জন্য একটি কালেকশন তৈরি করবে।
    '''
    serialzer = StudentSerializer(stu, many = True)
    print('serialzer', serialzer)
    # print('serialzer data', serialzer.data)
    json_data = JSONRenderer().render(serialzer.data)
    # print('json_data', json_data)
    return HttpResponse(json_data, content_type = 'application/json')
    '''
    return JsonResponse(serialzer.data, safe=False): এই লাইনে JsonResponse হলো Django-র একটি বিভিন্ন রেসপন্স ক্লাস, যা একটি JSON ফরম্যাটে ডাটা ফিরিয়ে দেয়। serialzer.data হলো সিরিয়ালাইজ করা ডাটা, এবং safe=False এটি সাধারণভাবে অবজেক্ট বা ডিকশনারি যাচাই করবে না এবং কোনও প্রকার ডাটা প্রয়োজনে এটি অনুমোদন দেবে।
    '''
    # return JsonResponse(serialzer.data, safe=False)

