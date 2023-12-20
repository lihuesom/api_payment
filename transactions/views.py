from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from models import Payment
from django.http import JsonResponse

@api_view(['POST'])
def paymentProcess(request):
    try: 
        new_payment = Payment(request)
        new_payment.save()
        return JsonResponse(new_payment)
    except Exception as e:
        Response({'message': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
