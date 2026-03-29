from django.http import JsonResponse
from .models import Product, Category


def products_list(request):
    products = Product.objects.all()
    return JsonResponse(list(products.values()), safe=False)


def product_detail(request, id):
    product = Product.objects.filter(id=id).values().first()
    if product:
        return JsonResponse(product)
    return JsonResponse({'error': 'Product not found'}, status=404)

def categories_list(request):
    categories = Category.objects.all()
    return JsonResponse(list(categories.values()), safe=False)


def category_detail(request, id):
    category = Category.objects.filter(id=id).values().first()
    return JsonResponse(category, safe=False)


def category_products(request, id):
    category = Category.objects.filter(id=id).first()
    if not category:
        return JsonResponse({'error': 'Category not found'}, status=404)

    products = category.products.all().values()
    return JsonResponse(list(products), safe=False)
