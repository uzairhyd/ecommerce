from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, *kwargs)
    #     print(context)
    #     return context

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = 'products/detail.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, *kwargs)
    #     print(context)
    #     return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product dose not exist.")
        return instance

def product_detail_view(request, pk=None):
    #queryset = Product.objects.get(pk=pk)
    # queryset = get_object_or_404(Product, pk=pk)
    # context = {
    #     'object': queryset
    # }
    # return render(request, "products/detail.html", context)

    #qs = Product.objects.filter(pk=pk)
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product dose not exist.")
    # if qs.exists() or qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product dosen't exist")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)

