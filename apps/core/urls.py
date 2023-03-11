from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views
from .api import ProviderViewSet



router = routers.SimpleRouter()

router.register('provider', ProviderViewSet, 'provider')

urlpatterns = router.urls