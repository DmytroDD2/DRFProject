from rest_framework import serializers

from contact_book.models import ContactBook, Events


class ContactBookSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['first_name'] == data['last_name']:
            raise serializers.ValidationError('the first and last name fields cannot be the same')
        return data

    class Meta:
        model = ContactBook
        fields = "__all__"


class ContactBook2Serializer(ContactBookSerializer):
    class Meta:
        model = ContactBook
        fields = ['id', 'first_name', 'last_name']


class EventsSerializer(serializers.ModelSerializer):
    contact_book = ContactBook2Serializer(many=True)


    class Meta:
        model = Events
        fields = '__all__'




    # def get_contact_book(self, obj):
    #     data = obj.contact_book.values('first_name', 'last_name', 'pk')
    #     return data

