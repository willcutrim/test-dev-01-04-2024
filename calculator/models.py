from django.db import models


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField("Tarifa da Distribuidora", blank=True, null=True)
    discount_rule = models.ForeignKey('RegrasDeDesconto', on_delete=models.CASCADE, verbose_name="Regra de Desconto")

    def calculate_savings(self):
        monthly_savings = self.consumption * self.distributor_tax * self.discount_rule * self.discount_rule.discount_value
        annual_savings = monthly_savings * 12

        return round(annual_savings, 2)

    def __str__(self) -> str:
        
        return f"{self.name} - {self.document}"

class RegrasDeDesconto(models.Model):

    
    CHOICES_CONSUMER = (
        ('COMERCIAL', 'Comercial'),
        ('RESIDENCIAL', 'Residencial'),
        ('INDUSTRIAL', 'Industrial'),
    )

    CHOICES_COVER = (
        ('90%', '90%'),
        ('95%', '95%'),
        ('99%', '99%'),
    )

    CHOICES_CONSUMPTION_RANGE = (
        ('< 10.000 kWh', '< 10.000 kWh'),
        ('>= 10.000 kWh e <= 20.000 kWh', '>= 10.000 kWh e <= 20.000 kWh'),
        ('> 20.000 kWh', '> 20.000 kWh'),
    )

    consumer_type = models.CharField(verbose_name="Tipo de Consumidor", choices=CHOICES_CONSUMER, max_length=128)
    consumption_range = models.CharField(verbose_name="Faixa de Consumo", choices=CHOICES_CONSUMPTION_RANGE, max_length=128)
    cover_value = models.CharField(verbose_name="Cobertura", choices=CHOICES_COVER, max_length=128)
    discount_value = models.FloatField(verbose_name="Desconto")


    def __str__(self) -> str:
        return f"{self.consumer_type} - {self.consumption_range} - {self.cover_value}"