from rest_framework import viewsets

from .permissions import IsAdminOrReadonly
from .serializers import ProductSerializer, CategorySerializer
from ...models import Product, Category
from utils import CustomPagination


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True)
    pagination_class = CustomPagination


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
    pagination_class = CustomPagination
