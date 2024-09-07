from django import forms
from .models import Product, Category, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price', 'brand']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
class RviewForm(forms.ModelForm):
    class Meta:
        model = Review
        feilds = ['content', 'rating']
        