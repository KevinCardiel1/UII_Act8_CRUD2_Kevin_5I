from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'precio': forms.NumberInput(attrs={'step': '0.01'})
        }
        labels = {
            'nombre': 'Nombre del producto',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'categoria': 'Categoría'
        }
