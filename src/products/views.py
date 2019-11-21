from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_detail_view(req, id):
    obj = Product.objects.get(id=id)
    context = {'object': obj}

    # untuk langsung semua
    # context = {'object' : obj}
    # return render(req, "product/detail.html", context)

    # bisa juga dalam folder aplikasinya
    return render(req, "products/product_detail.html", context)


def product_list_view(req):
    obj_list = Product.objects.all()
    context ={
        'object_list': obj_list
    }
    return render(req, "products/product_list.html", context)

# Form 1

def product_create_view(req):
    form = ProductForm(req.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    # untuk langsung semua
    context = {'form' : form}
    return render(req, "products/product_create.html", context)

def product_update_view(req, id):
    obj = get_object_or_404(Product, id= id)
    form = ProductForm(req.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    # print(form)
    # untuk langsung semua
    context = {'form' : form}
    return render(req, "products/product_create.html", context)

def product_delete_view(req, id):
    obj = get_object_or_404(Product, id= id)
    if req.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {'object': obj}
    return render(req, "products/product_delete.html", context)


# Form 2.
# def product_create_view(req):
#     form = RawProductForm()

#     if req.method == 'POST':
#         form = RawProductForm(req.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     # untuk langsung semua
#     context = {'form' : form}
#     return render(req, "products/product_create.html", context)



