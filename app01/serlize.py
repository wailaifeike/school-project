from rest_framework import serializers
from app01 import models

class NoticeSerializer(serializers.Serializer):
    username = serializers.CharField(source="user.username")
    title = serializers.CharField()
    id = serializers.IntegerField()
    status = serializers.CharField()
    ctime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    content = serializers.CharField()



