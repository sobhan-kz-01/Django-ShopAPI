from rest_framework.routers import DefaultRouter
from .views import ProductModelViewSet, CategoryModelViewSet

router = DefaultRouter()
router.register("",ProductModelViewSet, basename="product")
router.register("category",CategoryModelViewSet, basename="category")


urlpatterns = router.urls 
