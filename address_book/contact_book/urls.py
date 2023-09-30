from contact_book.views import ContactBookViewSet, EventsSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Events', EventsSet, basename='events')
router.register('', ContactBookViewSet, basename='contact_book')

urlpatterns = router.urls
