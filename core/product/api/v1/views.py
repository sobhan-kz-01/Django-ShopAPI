from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, CategorySerializer, ShortProductSerializer
from ...models import Product, Category
from utils import CustomPagination


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.filter(is_active=True)
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == "list":
            return ShortProductSerializer
        elif self.action == "retrieve":
            return ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
    pagination_class = CustomPagination
