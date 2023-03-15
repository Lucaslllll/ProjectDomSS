from rest_framework import status, viewsets, generics, mixins
from rest_framework.response import Response

from .models import Provider, Notes, Driver
from .serializers import (ProviderSerializer, DriverSerializer, NotesSerializer,
                            AllSerializer, ProviderExcludeSerializer)




class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = AllSerializer
    http_method_names = ['post', 'head', 'options']


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
    

# class ProviderGetViewSet(viewsets.ModelViewSet):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer
#     http_method_names = ['get', 'head', 'options']

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response({})


class ProviderListAPI(generics.GenericAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider

    def get(self, request, *args, **kwargs):
        lista = []
        # idNotes
        # idDriver
        for p in Provider.objects.all():
            d = Driver.objects.get(id=p.idDriver.id)
            n = Notes.objects.get(id=p.idNotes.id)
            driver = DriverSerializer(d)
            notes = NotesSerializer(n)
            dicF = {
                "providerName": p.providerName,
                "hour": p.hour,
                "quantity": p.quantity,
                "isConfirmedByHeritage": p.isConfirmedByHeritage,
                "isConfirmedByCPD": p.isConfirmedByCPD,
                "isConfirmedByArbitrator": p.isConfirmedByArbitrator,
                "loadType": p.loadType,
                "volumeType": p.volumeType,
                "isChecked": p.isChecked,
                "isReturned": p.isReturned,
                "isSchedule": p.isSchedule,
                "notes": notes.data,
                "driver": driver.data
            }
            lista.append(dicF)


        return Response(lista)