from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from contacts.models import Contact, ContactGroup

class ContactSerializer(serializers.ModelSerializer):
    # city = serializers.CharField(max_length=10, validators=[UniqueValidator(queryset=Contact.objects.all())])

    # def validate(self, data):
    #     if data['first_name'] == data['last_name']:
    #         raise serializers.ValidationError("lasjdfljasldf")
    #     return data


    # def validate_city(self, value):
    #     if value == 'ncorrect':
    #         raise serializers.ValidationError('City cannot be "Incorrect"')
    #     return value

    class Meta:
        model = Contact
        fields = '__all__'


class ContactGroupSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = ContactGroup
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
