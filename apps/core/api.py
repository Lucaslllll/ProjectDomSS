from rest_framework import status, viewsets, generics, mixins
from rest_framework.response import Response

from .models import Provider
from .serializers import ProviderSerializer




class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    
