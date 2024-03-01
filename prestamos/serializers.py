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

    # def validate_birthdate(self, value):
    #     value.micasa
    #     try:
    #         parsed_date = datetime.strptime(value.get('birthday'), DATE_FORMAT)
    #
    #     except ValueError:
    #         try:
    #             parsed_date = datetime.strptime(
    #                 value.get('birthday'), INVERSE_DATE_FORMAT)
    #         except ValueError:
    #             raise (ValueError("EL formato de fecha no es valido"))
    #
    #     return parsed_date
    #


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id', 'persona_id', 'prestamo_id', 'created_at')


class RawSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawSolicitud
        fields = ('id', 'origin', 'raw_data', 'solicitud_id')


class SolicitudDetalleSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    birthdate = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Solicitud
        fields = ('name', 'birthdate',
                  'amount', 'created_at')

    def get_name(self, obj):
        return obj.persona_id.name

    def get_birthdate(self, obj):
        return obj.persona_id.birthdate

    def get_amount(self, obj):
        return obj.prestamo_id.amount
