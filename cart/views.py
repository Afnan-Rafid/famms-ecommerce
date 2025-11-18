from django.shortcuts import render,HttpResponse
from product.models import Product

# Create your views here.
def cart(request):
    cart=Product.objects.all()
    return render(request,'cart1.html',{'Product':cart})