from django import forms
from news.models import Categories


class CreateCategoryModelForm(forms.Form):
    name = forms.CharField(
      label="Nome",
      max_length=200
    )

    class Meta:
        model = Categories
        fields = ["name"]
