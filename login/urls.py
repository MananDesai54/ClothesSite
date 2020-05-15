from django.urls import path,include
from .views import home,login,signup,logout,profile,a,search,changepassword,adminpanel,addproduct,removeProduct,editProduct,editProductPost
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',home,name='home'),
    path('a/',a,name='a'),
    path('adminpanel/',adminpanel,name='adminpanel'),
    path('adminpanel/addproduct/',addproduct,name='addproduct'),
    path('adminpanel/remove/<str:name>',removeProduct,name='removeproduct'),
    path('adminpanel/edit/<str:name>/',editProduct,name='editproduct'),
    path('adminpanel/editpost/<str:name>/',editProductPost,name='post'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout,name='logout'),
    path('profile/',profile,name='profile'),
    path('search/',search,name='search'),
    path('changepassword/',changepassword,name='chpass'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]