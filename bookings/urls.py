from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('contacts', views.ContactViewSet, basename='contacts')
router.register('properties', views.PropertyViewSet)
router.register('bookings', views.BookingViewSet)
router.register('carts', views.CartViewSet)

urlpatterns = router.urls