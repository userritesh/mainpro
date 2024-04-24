# api/serializers.py

# from rest_framework import serializers
# from .models import Student


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['name', 'roll_no', 'city']


# def create(self,validated_data):
#     return Student.objects.create(**validated_data)

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_no', 'city']
