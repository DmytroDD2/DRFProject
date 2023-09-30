
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from contacts.models import Contact, ContactGroup
from contacts.seriallizers import ContactSerializer, ContactGroupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import filters

from rest_framework.viewsets import ModelViewSet


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', "city"]
    # permission_classes = [IsAuthenticated]


class ContactGroupViewSet(ModelViewSet):
    queryset = ContactGroup.objects.prefetch_related("contacts").all()
    serializer_class = ContactGroupSerializer











# class ContactList(ListAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['first_name', 'last_name', "city"]
#     permission_classes = [IsAuthenticated]
#
#
#
# class ContactRetrieveList(RetrieveAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactUpdateList(UpdateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactDestroyList(DestroyAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#
#
# class ContactCreateList(CreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer











# class ContactList(APIView):
#
#     def get(self, request, format=None):
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



# class ContactsDetailView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Contact.objects.get(pk=pk)
#         except Contact.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         contacts = self.get_object(pk)
#         serializer = ContactSerializer(contacts)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         contacts = self.get_object(pk)
#         serializer = ContactSerializer(contacts, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         contacts = self.get_object(pk)
#         contacts.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
