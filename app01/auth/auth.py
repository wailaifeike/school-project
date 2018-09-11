from rest_framework.views import APIView
from rest_framework.response import Response
from app01 import models
import time
import uuid

class AuthView(APIView):
    def post(self,request,*agrs,**kwargs):
        print("post****************")
        ret = {"code":1000}
        username = request.data.get("username")
        password = request.data.get("password")
        print(username)
        user = models.UserInfo.objects.filter(username=username,password=password).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            models.UserToken.objects.update_or_create(user=user, defaults={'token': uid})
            ret['token'] = uid

        return Response(ret)
