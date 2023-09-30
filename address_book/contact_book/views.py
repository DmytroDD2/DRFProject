from django.shortcuts import render

from contact_book.models import ContactBook, Events
from contact_book.seriallizers import ContactBookSerializer, EventsSerializer
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet


class ContactBookViewSet(ModelViewSet):
    queryset = ContactBook.objects.all()
    serializer_class = ContactBookSerializer



class EventsSet(ModelViewSet):
    queryset = Events.objects.prefetch_related("contact_book").all()
    serializer_class = EventsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location']
