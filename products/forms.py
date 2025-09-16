from django import forms

from products.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label="nombre")
    description = forms.CharField(max_length=500, label="descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="precio")
    available = forms.BooleanField(initial=True, label="disponible", required=False)
    photo = forms.ImageField(required=False, label="foto")

    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data.get('photo')
        )