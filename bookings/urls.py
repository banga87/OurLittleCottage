from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('contacts', views.ContactViewSet, basename='contacts')
router.register('properties', views.PropertyViewSet)

properties_router = routers.NestedDefaultRouter(router, 'properties', lookup='property')
properties_router.register('guests', views.PropertyGuestViewSet, basename='property-guests')

urlpatterns = router.urls + properties_router.urls