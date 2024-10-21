# search/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('item', item_list, name='item_list'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('Product/', top_first, name='top_first'),
    path('Products/', get_items_by_brand, name='get_items_by_brand'),
    path('filter-items/', filter_items, name='filter_items'),
    path('get-items/', get_items, name='get_items'),
    path('', mainpage, name = 'mainpage')
]
