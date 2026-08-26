from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at',
        )
        model = Product
        # fields = '__all__'