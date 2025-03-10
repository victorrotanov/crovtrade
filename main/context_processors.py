from .models import Product, News


def global_context(request):
    return {
        "Product": Product.objects.all(),
        "News": News.objects.all(),
    }