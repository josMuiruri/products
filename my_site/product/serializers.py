from django.contrib.auth import get_user_model
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

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)