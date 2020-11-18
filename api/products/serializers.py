from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'title', 'price', 'code', 'quantity_in_stock')

# class UserSerializer(serializers.ModelSerializer):
#     products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'products']