from rest_framework import serializers
from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
    # client_name = serializers.CharField(source= 'client.name', read_only = True)
    class Meta:
        model = Sale
        # id_client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
        # id_product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
        # total = models.DecimalField(max_digits=8, decimal_places=2)
        # quantity = models.IntegerField(null=True, default=0, validators=[MinValueValidator(0)])
        # created = models.DateTimeField(default=timezone.now)
        fields = ['total', 'quantity']
