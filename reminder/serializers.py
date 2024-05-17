from rest_framework import serializers
from .models import Task, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']


class TaskSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Task
        fields = ['Title','user','Task_body','time','Done']

