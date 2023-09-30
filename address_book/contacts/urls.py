from contacts.views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact-group', ContactGroupViewSet, basename='contact_group')
router.register('', ContactViewSet, basename='contact')

urlpatterns = router.urls

#або

# urlpatterns = [
#     path('', ContactList.as_view(), name='contact_list') додаткова логіка
#     path('test', include(router.urls))
# ]










# urlpatterns = [
#     path('', ContactList.as_view(), name='contact_list'),
#     path('create/', ContactCreateList.as_view(), name='contact_create'),
#     path('<int:pk>', ContactRetrieveList.as_view(), name='contact_retrieve'),
#     path('<int:pk>/delete/', ContactDestroyList.as_view(), name='contact_destroy'),
#     path('<int:pk>/update/', ContactUpdateList.as_view(), name='contact_update')
# ]





















# from contacts.views import ContactList, ContactsDetailView
# from django.urls import path
#
# urlpatterns = [
#     path('', ContactList.as_view(), name='contact_list'),
#     path('detail/<int:pk>/', ContactsDetailView.as_view(), name='contact_detail')
# ]
