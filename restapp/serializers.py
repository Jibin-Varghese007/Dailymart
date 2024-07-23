from rest_framework import serializers
from.models import*

class Student1(serializers.Serializer):
  name = serializers.CharField(max_length=100)
  age = serializers.IntegerField()
  city = serializers.CharField(max_length=100)