from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Shop, Product
from .serializers import ShopSerializer, ShopsProductSerializer, ProductCreateSerializer


class ShopListView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetailView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopsProductSerializer


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product
