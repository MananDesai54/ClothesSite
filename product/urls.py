from django.urls import path
from .views import shop,product,men,women,cart,cart_show,remove,plus,minus,plus1,minus1,search,wishlist,wishlist_show,wishlistRemove,orders,orderCancel

urlpatterns = [
    path('',shop,name='shop'),
    path('men/',men,name='men'),
    path('women/',women,name='women'),
    path('cart/',cart_show,name='cart_show'),
    path('remove/<str:name>',remove,name='remove'),
    path('cart/<str:name>',cart,name='cart'),
    path('plus/<str:name>/',plus,name='plus'),
    path('minus/<str:name>/',minus,name='minus'),
    path('plus1/<str:name>/',plus1,name='plus'),
    path('minus1/<str:name>/',minus1,name='minus'),
    path('search/',search,name='search'),
    path('wishlist/<str:name>',wishlist,name='wishlist'),
    path('wishlist/',wishlist_show,name='wishlist_'),
    path('wishlist/remove/<str:name>',wishlistRemove,name='wishlistremove'),
    path('order/',orders,name='orders'),
    path('order/cancel/<str:name>',orderCancel,name='orderscancel'),
    path('<str:name>/',product,name='products'),
]