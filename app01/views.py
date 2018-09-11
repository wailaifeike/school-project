from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from app01 import models
from app01 import serlize


import os
import uuid
from schoolpro_demo import settings
import random

@csrf_exempt
def upload(request):
    if request.method == "OPTIONS":
        print("*******************")
        return HttpResponse("ok")

    if request.method == "POST":
        print(type(request.FILES))
        print('ok')
        # name =
        # print(type(name))
        from django.utils.datastructures import  MultiValueDict
        file_obj = request.FILES.get("upfile")
        print(file_obj)
        # name = uuid.uuid1()
        # print(name)
        b_list = range(100001, 100200)
        blist_webId = random.sample(b_list, 1)
        print(str(blist_webId[0])+file_obj.name)
        path = os.path.join(settings.MEDIA_ROOT, 'upfiles', str(blist_webId[0])+file_obj.name)
        print(path)
        with open(path, 'wb') as f:
            for line in file_obj:
                f.write(line)
        dic = {
            'error': 0,
            'url': "http://127.0.0.1:8010/media/upfiles/" + str(blist_webId[0])+file_obj.name,
            'message': ""
        }
        print(file_obj.name, type(file_obj))
        return JsonResponse(dic)

class NoticeView(APIView):
    def get(self,request,*args,**kwargs):
        ret = {"code":"1000"}
        try:
            notice_list = models.Notice.objects.all()
            # print(notice_list)
            bs = serlize.NoticeSerializer(instance=notice_list,many=True)
            for item in bs.data:
                if item.get("status") == "1":
                    item["status"] = "未审核"
                if item.get("status") == "2":
                    item["status"] = "审核中"
                if item.get("status") == "3":
                    item["status"] = "已发布"

            ret["data"]  = bs.data
        except Exception as e:
            ret["code"] = 1001
            ret["errors"] = "获取失败"

        return Response(ret)

    def post(self,request,*args,**kwargs):
        ret = {"code": "1000"}
        try:
            notice_data = request.data
            id = notice_data.get('id','1')
            # print("data",notice_data)
            # print("*args",args)
            # print("**kwargs",kwargs)
            models.Notice.objects.filter(pk=id).update(**notice_data)
        except Exception as e:
            ret['errors'] =e

        return Response(ret)



def test(request):
    print(request.POST.get("xx"))
    return HttpResponse('test("hello")')






