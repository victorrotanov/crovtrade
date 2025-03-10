from django.shortcuts import render
from django.http import JsonResponse
from .models import News, Product


def home(request):
    news = News.objects.all()
    return render(request, "content.html", {"News": news})


def get_news(request):
    news = News.objects.all().values("title", "content", "created_at")
    return JsonResponse({"content": "news", "data": list(news)})


def get_products(request):
    products = Product.objects.all().values("title", "start_price", "image")
    return JsonResponse({"content": "products", "data": list(products)})


def building_mixtures(request):
    return render(request, 'building_mixtures.html')


def metal_structures(request):
    return render(request, 'metal_structures.html')


def about_company(request):
    return render(request, 'about_company.html')


def contacts(request):
    return render(request, 'contacts.html')


def cement(request):
    return render(request, 'cement.html')


def stone(request):
    return render(request, 'stone.html')


def sand(request):
    return render(request, 'sand.html')


def vacancies(request):
    return render(request, 'vacancies.html')
