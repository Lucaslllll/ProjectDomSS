from rest_framework import status, viewsets, generics, mixins
from rest_framework.response import Response

from .models import Provider, Notes, Driver
from .serializers import ProviderSerializer, DriverSerializer, NotesSerializer, AllSerializer




class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = AllSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        driver = Driver(**serializer.data["driver"])
        driver.save()

        notes = Notes(**serializer.data["notes"])
        notes.save()

        provider = Provider(**serializer.data["provider"], idNotes=notes, idDriver=driver)
        provider.save()


        headers = self.get_success_headers(serializer.data)
        
        # sobreescrever para as infos cadastradas não retornem
        return Response({}, status=status.HTTP_201_CREATED, headers=headers)
    
