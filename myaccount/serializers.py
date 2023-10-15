from rest_framework import serializers
from .models import MyService






class MyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyService
        fields = ('service',)