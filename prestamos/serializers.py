from django.contrib.admin.utils import lookup_field
from rest_framework import serializers
from .models import Prestamo, Persona, Solicitud, RawSolicitud
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('id', 'amount')


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'name', 'birthdate')


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id', 'persona_id', 'prestamo_id', 'created_at')


class RawSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawSolicitud
        fields = ('id', 'origin', 'raw_data', 'solicitud_id')


# class RawLinkSerializer(serializers.HyperlinkedModelSerializer):
#     solicitud = serializers.HyperlinkedRelatedField(source='solicitud.id')
#
#     class Meta:
#         model = RawSolicitud
#         fields = ('solicitud', 'origin', 'raw_data')


class SolicitudDetalleSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()
    birthdate = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    source = serializers.HyperlinkedRelatedField(
        view_name='solicitud-detail',
        lookup_field='id',
        read_only=True
    )

    class Meta:
        model = Solicitud
        fields = ('id', 'name', 'birthdate',
                  'amount', 'created_at', 'url', 'source')

    def get_name(self, obj):
        return obj.persona_id.name

    def get_birthdate(self, obj):
        return obj.persona_id.birthdate.strftime("%d/%m/%Y")

    def get_amount(self, obj):
        return obj.prestamo_id.amount
