from rest_framework_nested import routers

from .views import ProductViewSet, ProductVariantViewSet

router = routers.DefaultRouter()
router.register("product", ProductViewSet, basename="product")

product_router = routers.NestedDefaultRouter(router, "product", lookup="product")
product_router.register("variants", ProductVariantViewSet, basename="variants")

urlpatterns = router.urls + product_router.urls
