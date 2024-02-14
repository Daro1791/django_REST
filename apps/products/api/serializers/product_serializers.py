from rest_framework import serializers
from apps.products.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state', 'created_data', 'modified_date', 'deleted_date')


