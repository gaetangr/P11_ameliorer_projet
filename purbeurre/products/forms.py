from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator

from purbeurre.products.models import Product


class ProductSearchForm(forms.ModelForm):
    """Form for searching a product to substituted."""

    input_user = forms.CharField(
        min_length=2,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Chercher un aliment"}),
    )
