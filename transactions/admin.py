from django.contrib import admin
from .models import Payment
# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname', 
        'card_number',
        'total_value', 
        'extra_description', 
        'comission_value', 
        )