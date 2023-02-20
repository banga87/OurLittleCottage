from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('guests', views.GuestViewSet, basename='guests')
router.register('properties', views.PropertyViewSet)
router.register('bookings', views.BookingViewSet)
router.register('carts', views.CartViewSet)

urlpatterns = router.urls