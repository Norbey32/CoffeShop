from django.urls import path
from products.views import ProductListView, ProductListAPI, ProductFormView


urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("api/", ProductListAPI.as_view(), name="list_product_api"),
    path("agregar/", ProductFormView.as_view(), name="add_product"),
]
