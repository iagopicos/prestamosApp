from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Persona, Prestamo, RawSolicitud, Solicitud
from .serializers import PersonaSerializer, PrestamoSerializer, SolicitudSerializer, RawSolicitudSerializer, SolicitudDetalleSerializer
from datetime import datetime


class Application(APIView):
    def post(self, request, format=None):
        data = request.data

        name = data.get('nombre')
        if name:  # We received from origin1
            first_name, second_name = data.get('apellidos').split(' ')
            origen = "origen1"
        else:  # We received from origin2
            name, first_name, second_name = data.get(
                'nombreCompleto').split(' ')
            origen = "origen2"
        fullname = " ".join([name, first_name, second_name])
        birth_date = data.get('fechaNacimiento')
        raw_data = str(request.data)
        amount = data.get('cantidad') or data.get('cantidadSolicitada')
        persona_serializer = PersonaSerializer(
            data={'name': fullname, 'birthdate': _parse_date(birth_date)})
        prestamo_serializer = PrestamoSerializer(data={'amount': amount})

        if persona_serializer.is_valid() and prestamo_serializer.is_valid():
            persona = persona_serializer.save()
            prestamo = prestamo_serializer.save()

            solicitud_serializer = SolicitudSerializer(
                data={"persona_id": persona.id, "prestamo_id": prestamo.id})
            if solicitud_serializer.is_valid():
                solicitud = solicitud_serializer.save()
                raw_solicitud = RawSolicitudSerializer(
                    data={"origin": origen, "raw_data": raw_data, "solicitud_id": solicitud.id})
                if raw_solicitud.is_valid():
                    raw_solicitud.save()
            detalle_serializer = SolicitudDetalleSerializer(solicitud,context={'request':request})
            return Response(detalle_serializer.data, status=status.HTTP_201_CREATED)
        return Response(persona_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrieveView(APIView):
    def get(self, request):
        lista_solicitudes = Solicitud.objects.all().order_by('-created_at')
        detalle_serializer = SolicitudDetalleSerializer(
            lista_solicitudes, many=True, context={'request': request})
        return Response(detalle_serializer.data, status=status.HTTP_200_OK)


class RetrieveRawData(APIView):
    def get(self, request, pk):
        raw_data = RawSolicitud.objects.get(solicitud_id=pk)

        raw_data_serializer = RawSolicitudSerializer(raw_data)
        return Response(raw_data_serializer.data, status=status.HTTP_200_OK)

# Function to parse the dates format we can have


def _parse_date(value):
    DATE_FORMAT = "%d/%m/%Y"
    INVERSE_DATE_FORMAT = "%Y/%m/%d"

    try:
        parsed_date = datetime.strptime(value, DATE_FORMAT).date()

    except ValueError:
        try:
            parsed_date = datetime.strptime(value, INVERSE_DATE_FORMAT).date()
        except ValueError:
            raise (ValueError("EL formato de fecha no es valido"))

    return parsed_date
