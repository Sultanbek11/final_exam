from rest_framework import serializers
from .models import Shop, Product


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class ShopsProductSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source="store.title")

    class Meta:
        model = Shop
        fields = "__all__"

        def get(self, request, format=None):
            serializer = ShopSerializer(Product.objects.all(), many=True)


# class ShopProductSerializer(serializers.ModelSerializer):
#     products = serializers.SerializerMethodField()
#
#     def get_products(self, obj):
#         return ShopsProductSerializer(obj.products.all(), many=True).data
#
#     class Meta:
#         model = Product
#         fields = ('title', 'products', 'price', 'quantity')


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'quantity')