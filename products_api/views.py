from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from products_api.models import Product
from products_api.serializers import ProductSerializer


@api_view(['GET'])
def api_root(request):
    return Response({
        "message": "Bem-vindo à Loja API 🛒",
        "version": "v1",
        "endpoints": {
            "token": "/api/v1/auth/token/",
            "products": "/api/v1/products/",
            "product_detail": "/api/v1/products/<id>/"
        }
    })


class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer