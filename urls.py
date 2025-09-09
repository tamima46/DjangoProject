from django.urls import path
from .views import ItemCreate, ItemList, ItemDetail

urlpatterns = [
    path('submit/', ItemCreate.as_view(), name='item-create'),
    path('search/', ItemList.as_view(), name='item-list'),
    path('update-delete/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]
