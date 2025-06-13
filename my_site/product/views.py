from django.http import JsonResponse
from . models import Product
from . serializers import ProductSerializer

# Create your views here.
def product_list(request):
    product = product.objects.all()
    serializer = ProductSerializer(product, many=True)