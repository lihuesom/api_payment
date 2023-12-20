from rest_framework import serializers
from .models import Payment
from django.core.validators import MinValueValidator

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        extra_kwargs = {
            'total_value': {'validators': [MinValueValidator(limit_value=100000)]},
            'comission_value': {'read_only': True},
        }
    
    def create(self, validated_data):
        new_payment = Payment(
            name=self.data.get('name'),
            surname=self.data.get('surname'),
            card_number=self.data.get('card_number'),
            card_cvv=self.data.get('card_cvv'),
            total_value=self.data.get('total_value'),
            extra_description=self.data.get('extra_description')
        )
        new_payment.comission()
        return new_payment