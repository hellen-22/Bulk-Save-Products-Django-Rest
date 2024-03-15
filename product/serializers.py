from rest_framework import serializers
from .models import Product, ProductVariant


class AddProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id',  'sku', 'name', 'price', 'details']


class CreateAndListProductsSerializer(serializers.ModelSerializer):
    variants = AddProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'variants']

    def create(self, validated_data):
        variants = validated_data.pop('variants')
        product = Product.objects.create(**validated_data)

        product_variants = [ProductVariant(product=product, **item,) for item in variants]

        ProductVariant.objects.bulk_create(product_variants)

        return product

class UpdateAndDeleteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image']


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'sku', 'name', 'price', 'details']

    def create(self, validated_data):
        product_id = self.context['product_id']
        product = Product.objects.get(id=product_id)

        variant = ProductVariant.objects.create(product=product, **validated_data)

        return variant
