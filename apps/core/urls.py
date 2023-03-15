from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views
from .api import ProviderViewSet, ProviderListAPI



router = routers.SimpleRouter()

router.register('provider', ProviderViewSet, 'provider')

urlpatterns = router.urls


urlpatterns += [
	path('provider-list', ProviderListAPI.as_view(), name='provider list'),
	
]