from rest_framework import  serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    product_manufacturing_date = serializers.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Product
        fields = '__all__'
        
    def create(self, validated_data):
        obj, created = Product.objects.get_or_create(**validated_data)
        return obj