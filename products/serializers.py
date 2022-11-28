from rest_framework import serializers
from .models import Shop, Product


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

        def get(self, request, format=None):
            serializer = ShopSerializer(Product.objects.all(), many=True)


class BuyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def get_obj(self, pk):
        if pk in Product.pk:
            return Product.objects.get(pk=pk)
        else:
            raise ('Нет в наличии')
