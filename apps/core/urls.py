from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views
from .api import ProviderViewSet, ProviderListAPI, ProviderUpdateAPI, ProviderDeleteAPI, ProviderFilterDateAPI



router = routers.SimpleRouter()

router.register('provider', ProviderViewSet, 'provider')

urlpatterns = router.urls


urlpatterns += [
	path('provider-list', ProviderListAPI.as_view(), name='provider list'),
	path('provider-update/<int:pk>', ProviderUpdateAPI.as_view(), name='provider update'),
	path('provider-delete/<int:pk>', ProviderDeleteAPI.as_view(), name='provider remove'),
	path('provider-date', ProviderFilterDateAPI.as_view(), name='provider filter date')

]