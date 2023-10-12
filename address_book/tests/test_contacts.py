import json

from django.db import IntegrityError
from django.test import TestCase
import pytest
from django.urls import reverse
from pytest_mock import mocker
from rest_framework.test import APIClient
from django.test import TestCase

from contacts.models import Contact

from contacts.models import Contact, ContactActivityLog, ContactGroup
from contacts.seriallizers import ContactSerializer, ContactGroupSerializer
from contacts.views import ContactViewSet
from unittest.mock import Mock, call
from rest_framework import serializers
@pytest.fixture
def api_clint():
    return APIClient()


@pytest.fixture
def contact_factory():
    def factory(**data):
        return Contact.objects.create(**data)

    return factory


@pytest.mark.django_db
def test_filter_by_first_name(api_clint, contact_factory):
    contacts1 = contact_factory(first_name="Dmytro", city="Lviv")
    contacts2 = contact_factory(first_name="Anton", city="Kyiv")

    response = api_clint.get(reverse("contact-list"), {"first_name": "Dmytro"})

    assert response.status_code == 200
    assert len(response.data) == 1

    assert response.data[0]['first_name'] == contacts1.first_name


@pytest.mark.django_db
def test_filter_by_city(api_clint, contact_factory):
    contacts1 = contact_factory(first_name="Dmytro", city="Lviv")
    contacts2 = contact_factory(first_name="Anton", city="Kyiv")

    response = api_clint.get(reverse("contact-list"), {"city": "Kyiv"})

    assert response.status_code == 200
    assert len(response.data) == 1

    assert response.data[0]['first_name'] == contacts2.first_name




@pytest.fixture
def contact():
    return Contact.objects.create(
        first_name="John",
        last_name="Doe",
        country="USA",
        city="NY",
        street="Main street",
        url="https://example.com",
        phone="+1234567890",
        image=None  # можна додати зображення, якщо потрібно
    )


@pytest.mark.django_db
def test_contact_serializer(contact):
    serialized = ContactSerializer(contact)

    assert serialized.data["first_name"] == "John"
    assert serialized.data["last_name"] == "Doe"
    assert serialized.data["country"] == "USA"
    assert serialized.data["city"] == "NY"
    assert serialized.data["street"] == "Main street"
    assert serialized.data["url"] == "https://example.com"
    assert serialized.data["phone"] == "+1234567890"
    assert serialized.data["image"] is None  # якщо у вас є зображення, перевірте його URL тут


@pytest.mark.django_db
def test_contact_creation_creates_activity_log(contact):
    activity_logs = ContactActivityLog.objects.filter(contact=contact)
    activity_log = activity_logs.first()

    assert activity_log.activity_type == 'CREATED'
    assert activity_log.timestamp is not None
    assert activity_log.contact == contact


@pytest.mark.django_db
def test_contact_creation_change_activity_log(contact):
    contact.first_name = 'Janeadasfas'
    contact.save()
    activity_logs = ContactActivityLog.objects.filter(contact=contact)
    activity_log = activity_logs.last()

    assert activity_log.activity_type == 'EDITED'
    assert activity_log.timestamp is not None
    assert activity_log.contact == contact

    updated_contact = Contact.objects.get(id=contact.id)
    assert updated_contact.first_name == 'Janeadasfas'
    assert updated_contact.last_name == 'Doe'


@pytest.fixture
def mock_contact_delete(mocker):
    return mocker.patch.object(ContactViewSet, 'destroy')

@pytest.mark.django_db
def test_delete_contact(mock_contact_delete, contact):

    mock_contact_delete(contact)
    is_contact_delete = Contact.objects.filter(pk=contact.pk).exists()
    assert mock_contact_delete.call_args_list == [call(contact)]
    assert mock_contact_delete.call_count == 1
    assert is_contact_delete is True



@pytest.fixture
def mock_contact_create(mocker):
    return mocker.patch.object(ContactViewSet, 'create')


@pytest.mark.django_db
def test_create_contact_without_saving(mock_contact_create):
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'country': 'USA',
        'city': 'NY',
        'street': 'Main street',
    }

    mock_contact_create(data)
    assert mock_contact_create.call_args_list == [call(data)]
    assert mock_contact_create.call_count == 1









@pytest.mark.django_db
def test_create_group(contact):
    group = ContactGroup.objects.create(name='lasdjflajfljasldfkjasdf')
    group.contacts.add(contact)
    assert contact in group.contacts.all()





@pytest.fixture
def contact_ser():
    contact1 = Contact.objects.create(first_name="John", city="NY")
    contact2 = Contact.objects.create(first_name="Jane", city="LA")
    group = ContactGroup.objects.create(name='lasdjflajfljasldfkjasdf')
    group.contacts.add(contact1, contact2)
    return group

@pytest.mark.django_db
def test_group_serializer(contact_ser):
    serialized = ContactGroupSerializer(contact_ser).data
    json_data = json.dumps(serialized)

    deserialized_data = json.loads(json_data)
    assert deserialized_data['name'] == 'lasdjflajfljasldfkjasdf'
    assert len(deserialized_data['contacts']) == 2

    for contact_data in serialized['contacts']:
        contact = Contact.objects.get(id=contact_data['id'])

        assert contact_data['first_name'] == contact.first_name


@pytest.mark.django_db
def test_create_contact_raises():
    Contact.objects.create(first_name='John', last_name='Doe', city='NY')

    with pytest.raises(IntegrityError):
        Contact.objects.create(first_name='John', last_name='Doe', city='VY')













































# class TestContactFilter(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.client = APIClient
#         Contact.objects.create(first_name="John", city="NY")
#         Contact.objects.create(first_name="Jane", city="LA")
#
#     def test_filter_by_first_name(self):
#         url = reverse("contact-list")
#         response = self.client.get(url, {"first_name": "John"})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]["first_name"], "John")
#
#     def test_filter_by_city(self):
#         url = reverse("contact-list")
#         response = self.client.get(url, {"city": "NY"})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]["city"], "NY")


