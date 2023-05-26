from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,PrductViewSet,PurchaseViewSet


router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
router.register(r'product', PrductViewSet, basename="product")
router.register(r'purchase', PurchaseViewSet, basename="purchase")

urlpatterns = [
    path("", include(router.urls))
]