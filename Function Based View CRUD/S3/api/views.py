from django.shortcuts import render
from .models import Student
from .serializers import StudentSeralizer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id)
            serilaizer = StudentSeralizer(stu)
            json_data = JSONRenderer().render(serilaizer.data)
            return HttpResponse(json_data, content_type = 'application/json')

        stu = Student.objects.all()
        serilaizer = StudentSeralizer(stu, many = True)
        json_data = JSONRenderer().render(serilaizer.data)
        return HttpResponse(json_data, content_type = 'application/json')



    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSeralizer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res ={'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        '''
        partial=True: এই প্যারামিটারটি পার্শিয়াল আপডেট অনুমোদন করা হয়েছে কিনা তা নির্দেশ করে। True হলে, এটি ইনকামিং ডেটার মধ্যে যে কোন ক্ষেত্র আপডেট করতে অনুমতি দেয়। এটি মাধ্যমে আপনি একটি কিছু ফিল্ড মাত্র আপডেট করতে পারেন যেগুলি ইনকামিং ডেটা থেকে প্রদান করা হয়েছে।
        Partial Update mean  All data not required
        '''
        serializer = StudentSeralizer(stu, data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data update successful'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type ='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type ='application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deleted'}
        '''
         json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')
        লাইনটির পরিবর্তে  এটি লেখা যায়
        return JsonResponse(res, safe=False)
        '''
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type = 'application/json')
        '''
        res: এটি হলো সে ডেটা বা অবজেক্ট যা আপনি জবাবে ফর্ম্যাট করতে চান এবং এটি যে JSON অবজেক্ট হবে তা নির্দেশ করে।

        safe=False: এই প্যারামিটারটি নির্দিষ্ট করে যে, ডেটা একটি JSON-serializable অবজেক্ট হোক না কেন, এটি সত্য হোক না। এটি কোনো পাইথন অবজেক্টকে জেসনে রূপান্তর করতে পারে না, তখন safe=False হয়ে থাকে।
        '''
        return JsonResponse(res, safe=False)


    


        




