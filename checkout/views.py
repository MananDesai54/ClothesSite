from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import CartProducts
from .models import OrderDetails
from django.contrib import messages

# Create your views here.
def checkout(request):
    if request.user.is_authenticated:
        cart = CartProducts.objects.filter(username=request.user.username)
        list1 = []
        total = 0
        for c in cart:
            total+=c.price
        return render(request,'checkout.html',{'products':cart,'total':total})
    else:
        return redirect('/')

def detail(request):
    if request.method == 'POST':
        address = request.POST['address']
        sub_address = request.POST['sub-address']
        city = request.POST['city']
        country = request.POST['country']
        state = request.POST['state']
        pincode = request.POST['pincode']

        cart = CartProducts.objects.filter(username=request.user.username)
        for c in cart:
            if OrderDetails.objects.filter(username=request.user.username,product_name=c.product_name).exists():
                order = OrderDetails.objects.filter(username=request.user.username,product_name=c.product_name)[0]
                order.quantity = str(int(order.quantity)+int(c.quantity))
            else:
                order = OrderDetails(username=request.user.username,product_name=c.product_name,address=address,sub_address=sub_address,city=city,country=country,state=state,pincode=pincode,price=c.price,quantity=c.quantity,imagepath=c.imagePath)
            order.save()
            c.delete()
            messages.info(request,'Ordered Successfully.')
        return redirect('/')