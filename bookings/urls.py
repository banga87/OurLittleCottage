from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('contacts', views.ContactViewSet, basename='contacts')
router.register('properties', views.PropertyViewSet)

urlpatterns = router.urls