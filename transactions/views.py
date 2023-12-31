from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db import IntegrityError
from .serializers import PaymentSerializer
from creditcard import CreditCard

@api_view(['POST'])
#@authentication_classes([]) 
#@permission_classes([AllowAny])
def paymentProcess(request):
    try: 
        card_number = request.data.get('card_number')
        card = CreditCard(card_number)
        #if card.is_valid:
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Pago registrado correctamente','Tarjeta': card.brand}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'message': 'Error en los datos del pago', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError as e:
        return Response({'message': 'Error al registrar el pago: {}'.format(str(e))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'message': 'Error desconocido: {}'.format(str(e))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
