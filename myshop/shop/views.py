from django.shortcuts import render

from . models import Product

# Create your views here.
def product_detail(request):
    #получить product из product
    all_product = Product.objects.all()
    print(all_product)
    return render(request, 'shop/list.html', {'all_product': all_product})