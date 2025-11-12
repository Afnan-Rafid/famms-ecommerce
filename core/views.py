from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def index(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def blog(request):
    return render(request,'blog_list.html')

def about(request):
    return render(request,'about.html')

def testimonial(request):
    return render(request,'testimonial.html')

def contact(request):
    return render(request,'contact.html')
