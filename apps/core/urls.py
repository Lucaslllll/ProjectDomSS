from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views
from .api import ProviderViewSet, ProviderGetViewSet



router = routers.SimpleRouter()

router.register('provider', ProviderViewSet, 'provider')
router.register('provider/list', ProviderGetViewSet, 'provider list')

urlpatterns = router.urls