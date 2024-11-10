from django.forms import ModelForm, CharField, TextInput, Form, ChoiceField
from .models import ProductModel, ProductCategory


class GetProductByCategoryForm(Form):
    product_category = ChoiceField(
        choices=ProductCategory, required=True, label="Category"
    )

    category = ChoiceField()


class CreateProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
        exclude = ("user", "date_of_pub")


class SearchForm(Form):
    search = CharField(
        max_length=100, widget=TextInput(attrs={"placeholed": "Search Product"})
    )
