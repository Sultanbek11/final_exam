from django.urls import path
from .views import ShopListView, ShopDetailView, ProductCreateAPIView


urlpatterns = [
    path('all_store/', ShopListView.as_view()),
    path('store/<int:pk>/', ShopDetailView.as_view()),
    path('create_product/', ProductCreateAPIView.as_view()),
]