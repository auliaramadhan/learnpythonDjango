from django.shortcuts import render

from .models import Product

# Create your views here.
def product_detail_view(req):
    obj = Product.objects.get(id=1)
    context = {"title": obj.title, "desc": obj.desc}
    return render(req, "product/detail.html", context)

