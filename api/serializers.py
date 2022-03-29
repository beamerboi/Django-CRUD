from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = '__all__'