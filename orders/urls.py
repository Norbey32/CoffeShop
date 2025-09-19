from django.urls import path
from .views import OrderView, CreatedOrderProductView

urlpatterns = [
    path('mi-orden', OrderView.as_view(), name="my_order"),
    path('agregar-producto', CreatedOrderProductView.as_view(), name="add_product"),
]
