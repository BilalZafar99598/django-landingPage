from django.urls import path
from .views import Index,Prod,brand_product_list


urlpatterns=[
    path('',Index.as_view(),name='index'),
    path('products/<int:brand_id>',brand_product_list,name="Products"),
    path('stock/<int:brand_id>',brand_product_list,name="Products"),
]