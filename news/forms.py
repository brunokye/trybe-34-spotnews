from django import forms
from news.models import Categories, News, Users


class CreateCategoryModelForm(forms.Form):
    name = forms.CharField(
      label="Nome",
      max_length=200
    )

    class Meta:
        model = Categories
        fields = ["name"]


class CreateNewsModelForm(forms.Form):
    title = forms.CharField(label="Título")
    content = forms.CharField(label="Conteúdo", widget=forms.Textarea)
    author = forms.ModelChoiceField(
        label="Autoria", queryset=Users.objects.all()
    )
    created_at = forms.DateField(
        label="Criado em", widget=forms.DateInput(attrs={"type": "date"})
    )
    image = forms.ImageField(label="URL da Imagem")

    class Meta:
        model = News
        fields = ["title", "content", "author", "created_at", "image"]
