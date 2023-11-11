from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadonly
from .serializers import ProductSerializer, CategorySerializer
from ...models import Product, Category
from utils import CustomPagination

class ProductModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadonly]
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True)
    pagination_class = CustomPagination


class CategoryModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadonly]
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
    pagination_class = CustomPagination