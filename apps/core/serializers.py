from rest_framework import serializers
from .models import Provider, Driver, Notes



class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        exclude = ("idNotes", "idDriver", )


class AllSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()
    notes = NotesSerializer()
    provider = ProviderSerializer()

    class Meta:
        model = Provider
        fields = ['provider', 'notes', 'driver']

