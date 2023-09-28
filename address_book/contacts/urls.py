from contacts.views import ContactList, ContactsDetailView
from django.urls import path

urlpatterns = [
    path('', ContactList.as_view(), name='contact_list'),
    path('detail/<int:pk>/', ContactsDetailView.as_view(), name='contact_detail')
]
