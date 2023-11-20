from rest_framework import viewsets

from .permissions import IsAdminOrReadonly
from .serializers import ProductSerializer, CategorySerializer, ShortProductSerializer
from ...models import Product, Category
from utils import CustomPagination


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Product.objects.filter(is_active=True)
    pagination_class = CustomPagination
    
    def get_serializer_class(self):
        if self.action == "list":
            return ShortProductSerializer
        elif self.action == "retrive":
            return ProductSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
    pagination_class = CustomPagination
