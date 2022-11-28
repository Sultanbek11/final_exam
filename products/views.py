from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Shop, Product
from .serializers import ShopSerializer, BuyProductSerializer

class ShopViewSet(ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()


    @action(detail=True, methods=['POST'], name='buy', url_name='buy')
    def buy(self, pk):
        buy = Product.objects.get(pk=pk)
        serializer = BuyProductSerializer.get_obj(pk=pk)
        if serializer.is_valid():
            prod = Product.objects.get(pk)
            prod =


