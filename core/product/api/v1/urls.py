from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register("", ProductViewSet, basename="product")
router.register("category", CategoryViewSet, basename="category")


urlpatterns = router.urls
