from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Student

#using ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    #using 'validators' 
    # def starts_with(value):
    #     if value[0].lower() != 'r':
    #         raise serializers.ValidationError('Name should start with R')
    #for using validators we need to use explicit declaration in model serializer
    # name = serializers.CharField(validators = [starts_with])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # fields = '__all__'
        # read_only_fields = ['name', 'roll'] # value of 'name' and 'roll' will not change in any update operation
        # extra_kwrgs = {'name' : {'read_only':True}}    # another way of wriiting read_only property
    
    # Field Vlidation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value

    #Object Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() == 'ranchi':
            raise serializers.ValidationError('City should be ranchi')
        return data

    


# class StudentSerializer(serializers.Serializer):

    # name = serializers.CharField(max_length = 100)
    # roll = serializers.IntegerField()
    # city = serializers.CharField(max_length = 100)

    # Field validation
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat full')
    #     return value

    # Object Validation
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'rohit' and ct.lower() == 'ranchi':
    #         raise serializers.ValidationError('City should be ranchi')
    #     return data 

    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     print(instance.name)
    #     instance.name = validated_data.get('name', instance.name)
    #     print(instance.name)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.save()
    #     return instance