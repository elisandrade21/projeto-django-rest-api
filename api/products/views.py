from rest_framework import viewsets
from .models import Products
from .serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
