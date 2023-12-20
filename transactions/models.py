from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nombre')
    surname = models.CharField(max_length=255,verbose_name='Apellido')
    card_number = models.CharField(max_length=16,verbose_name='Número de tarjeta')
    card_cvv = models.CharField(max_length=3,verbose_name='Código de seguridad')
    total_value = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(limit_value=100000)],verbose_name='Total')
    extra_description = models.TextField(null=True,blank=True,verbose_name='Observaciones')
    comission_value = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Comisión')

    def comission(self, *args, **kwargs):
        #Por cada pago ingresado se cobra el 3% + IVA.
        comission_rate = 0.03  # 3%
        iva_rate = 0.19  # 19%
        retencion_rate = 0.015  # 1.5%

        # Calcular la retención en la fuente
        retencion_amount = float(self.total_value) * retencion_rate

        # Restar la retención al total
        total_after_retencion = float(self.total_value) - retencion_amount

        # Calcular la comisión sin IVA
        comission_without_iva = total_after_retencion * comission_rate

        # Calcular el IVA de la comisión
        iva_amount = comission_without_iva * iva_rate

        # Calcular la comisión total con IVA después de la retención
        self.comission_value = comission_without_iva + iva_amount
        self.save()

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['-id']

    def __str__(self):
        return f"{self.name} {self.surname} - {self.total_value}"