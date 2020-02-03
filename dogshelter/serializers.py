from rest_framework import serializers
from .models import Dogs


#here we add field doc_info which is calculated from fields byname and breed
class DogsSerializer(serializers.ModelSerializer):
    doc_info = serializers.SerializerMethodField('get_doc_info')

    def get_doc_info (self, obj):
        return obj.byname + obj.breed
    class Meta:
        model = Dogs
        fields = ('byname', 'age', 'breed', 'doc_info')
    
#functions for API
    def create (self, validated_data):
        return Dogs.objects.create(**validated_data)

    def update (self, instance, validated_data):
        instance.byname = validated_data.get('byname', instance.byname)
        instance.age = validated_data.get('age', instance.age)
        instance.breed = validated_data.get('breed', instance.breed)

        instance.save()
        return instance


