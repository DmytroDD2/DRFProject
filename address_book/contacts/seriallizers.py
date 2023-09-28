from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'








# class Post:
#     def __init__(self, name: str, description: str, created_at=None):
#         self.name = name
#         self.description = description
#         self.created_at = created_at or datetime.now()
#
#
# class PostSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=155)
#     description = serializers.CharField()
#     created_at = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Post(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.description = validated_data.get('description')
#         instance.created_at = validated_data.get('created_at')
#         return instance
