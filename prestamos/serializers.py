from rest_framework import serializers
from .models import Prestamo, Persona, Solicitud, RawSolicitud


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('id', 'amount')


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'name', 'firstname', 'secondname')


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id', 'persona_id', 'prestamo_id', 'created_at')


class RawSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawSolicitud
        fields = ('id', 'origin', 'raw_data')
