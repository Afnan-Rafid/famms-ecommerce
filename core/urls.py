from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name = 'base'),
    path('index', views.index, name = 'index'),
    path('product',views.product,name='product'),
    path('blog',views.blog,name='blog'),
    path('about',views.about,name='about'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('contact',views.contact,name='contact')
]

