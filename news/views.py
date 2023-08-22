from django.shortcuts import render, redirect
from news.models import News, Categories
from news.forms import CreateCategoryModelForm, CreateNewsModelForm


def home(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, 'home.html', context)


def news_details(request, id):
    news = News.objects.get(id=id)
    context = {"news": news}
    return render(request, 'news_details.html', context)


def categories_form(request):
    form = CreateCategoryModelForm()

    if request.method == "POST":
        form = CreateCategoryModelForm(request.POST)

        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "categories_form.html", context)


def news_form(request):
    form = CreateNewsModelForm()
    categories = Categories.objects.all()

    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)

        if form.is_valid():
            News.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form, "categories": categories}

    return render(request, "news_form.html", context)
