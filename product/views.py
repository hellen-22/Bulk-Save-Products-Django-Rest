from rest_framework.viewsets import ModelViewSet

from .models import Product, ProductVariant
from .serializers import CreateAndListProductsSerializer, UpdateAndDeleteProductSerializer, ProductVariantSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['POST', 'GET']:
            return CreateAndListProductsSerializer
        return UpdateAndDeleteProductSerializer
        

class ProductVariantViewSet(ModelViewSet):
    serializer_class = ProductVariantSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

    def get_queryset(self):
        return ProductVariant.objects.filter(product_id=self.kwargs['product_pk'])
    