from django.urls import path
from .import views

urlpatterns = [
    path('prestamo/', views.Application.as_view(), name='prestamo'),
    path('solicitudes/', views.RetrieveView.as_view(), name='solicitudes'),
    path('raw/<int:pk>', views.RetrieveRawData.as_view(), name='solicitud-detail')
]
