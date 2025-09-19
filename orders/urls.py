from django.urls import path
from .views import OrderView

urlpatterns = [
    path('mi-orden', OrderView.as_view(), name="my_order")
]
