from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Product,Cart,CartProducts,WishList
from checkout.models import OrderDetails
from django.contrib import messages

global quantity1
quantity1 = 1
global len1
len1 = ''
def shop(request):
    product = Product.objects.all()
    global len1
    return render(request,'shop.html',{'products':product,'len':len1})

def product(request,name):
    product = get_object_or_404(Product,product_name=name)
    catagory = product.catagory
    products = Product.objects.all().filter(catagory=catagory)
    global len1
    return render(request,'product.html',{'product':product,'products':products,'quantity1':quantity1,'len':len1})

def men(request):
    product = Product.objects.all().filter(catagory='Men')
    return render(request,'shop.html',{'products':product,'len':len1})

def women(request):
    product = Product.objects.all().filter(catagory='Women')
    return render(request,'shop.html',{'products':product,'len':len1})

# dict1 = {}
# user1 = None
# list1 = []
# def cart(request,name):
#     list1.clear()
#     product = Product.objects.get(product_name=name)
#     user1 = request.user.username
#     list1.append(product)
#     print(product)
#     print(list1)
#     if user1 in dict1:
#         print('already')
#         if product in dict1[user1]:
#             pass
#         else:
#             dict1[user1].append(product)
#     else:
#         print('new')
#         dict1[user1] = list1
#     print(dict1)
#     return render(request,'cart.html',{'products':dict1[user1]})
def cart(request,name):
    global quantity1
    current = request.user.username
    cartAll = Cart.objects.all()
    product = Product.objects.get(product_name=name)
    flag = True
    for cart in cartAll:
        if current == cart.user.username:
            flag = True
            break
        else:
            flag = False
    if not bool(cartAll) or not flag:
        user = User.objects.get(username=current)
        cart = Cart(user=user)
        cart.save()
    if not CartProducts.objects.filter(username=current,product_name=product.product_name).exists():
        cartProduct = CartProducts(username=current,product_name=product.product_name,price=product.price,quantity=quantity1,imagePath=product.img1.url)
        cartProduct.save()
    else:
        products1 = CartProducts.objects.filter(username=current,product_name=product.product_name)[0]
        quantity = int(products1.quantity)+quantity1
        products1.quantity = str(quantity)
        products1.price = str(int(product.price * quantity))
        products1.save()
        #CartProducts.objects.all().update()
    products = CartProducts.objects.filter(username=current)
    quantity1 = 1
    if bool(products):
        # return render(request,'cart.html',{'products':products})
        return redirect('/shop/cart/')
    return render(request,'cart.html',{'products':None})

# def cart_show(request):
#     user1 = request.user.username
#     if bool(dict1):
#         if bool(dict1[user1]):
#             return render(request,'cart.html',{'products':dict1[user1]})
#     return render(request,'cart.html',{'products':None})

def cart_show(request):
    user1 = request.user.username
    products = CartProducts.objects.filter(username=user1)
    global len1
    len1 = len(products)
    if len1 == 0:
        len1 = ''
    if bool(products):
        total = 0
        for product in products:
            total += product.price
        return render(request,'cart.html',{'products':products,'total':total,'len':len1})
    return render(request,'cart.html',{'products':None})

# def remove(request,name):
#     user1 = request.user.username
#     product = Product.objects.get(product_name=name)
#     dict1[user1].remove(product)
#     print(dict1)
#     return redirect('/shop/cart')

def remove(request,name):
    user1 = request.user.username
    product = Product.objects.get(product_name=name)
    cartProduct = CartProducts.objects.get(username=user1,product_name=product.product_name)
    if cartProduct.quantity > 1:
        cartProduct.quantity = int(cartProduct.quantity)-1
        cartProduct.price = str(int(product.price) * int(cartProduct.quantity))
        cartProduct.save()
    elif cartProduct.quantity == 1 :
        cartProduct.delete()
    flag = CartProducts.objects.filter(username=user1).exists()
    if flag==False:
        cartAll = Cart.objects.all()
        for cart in cartAll:
            if cart.user.username == user1:
                cart.delete()
    products = CartProducts.objects.filter(username=user1)
    if bool(products):
        return redirect('/shop/cart/')
        #return render(request,'cart.html',{'products':products})
    return redirect('/shop/cart/')
    #return render(request,'cart.html',{'products':None})

def plus(request,name):
    # user1 = request.user.username
    # product = Product.objects.get(product_name=name)
    # if CartProducts.objects.filter(username=user1,product_name=product.product_name).exists():
    #     cartProduct = CartProducts.objects.get(username=user1,product_name=product.product_name)
    #     cartProduct.quantity = str(int(cartProduct.quantity)+1)
    #     cartProduct.save()
    global quantity1
    quantity1 += 1
    return redirect(f'/shop/{name}')

def minus(request,name):
    # user1 = request.user.username
    # product = Product.objects.get(product_name=name)
    # cartProduct = CartProducts.objects.get(username=user1,product_name=product.product_name)
    # cartProduct.quantity = str(int(cartProduct.quantity)-1)
    # cartProduct.save()
    global quantity1
    if quantity1 > 1:
        quantity1 -= 1
    return redirect(f'/shop/{name}')

def plus1(request,name):
    user1 = request.user.username
    product = Product.objects.get(product_name=name)
    cartProduct = CartProducts.objects.get(username=user1,product_name=product.product_name)
    cartProduct.quantity = str(int(cartProduct.quantity)+1)
    cartProduct.price = str(int(product.price) * int(cartProduct.quantity))
    cartProduct.save()
    return redirect('/shop/cart')

def minus1(request,name):
    user1 = request.user.username
    product = Product.objects.get(product_name=name)
    cartProduct = CartProducts.objects.get(username=user1,product_name=product.product_name)
    if cartProduct.quantity > 1:
        cartProduct.quantity = str(int(cartProduct.quantity)-1)
        cartProduct.price = str(int(product.price) * int(cartProduct.quantity))
        cartProduct.save()
    return redirect('/shop/cart')

def search(request):
    return render(request,'shop.html',{})

def wishlist(request,name):
    user = request.user.username
    product = Product.objects.get(product_name=name)
    if not WishList.objects.filter(username=user,product_name=product.product_name).exists():
        wishlist = WishList(username=user,product_name=product.product_name,price=product.price,imagePath=product.img1.url)
        wishlist.save()
    return redirect('/shop/wishlist')

def wishlist_show(request):
    user1 = request.user.username
    products = WishList.objects.filter(username=user1)
    global len1
    len1 = len(products)
    if len1 == 0:
        len1 = ''
    if bool(products):
        return render(request,'wishlist.html',{'products':products,'len':len1})
    return render(request,'wishlist.html',{'products':None})

def wishlistRemove(request,name):
    user = request.user.username
    product = Product.objects.get(product_name=name)
    wishListProcuct = WishList.objects.get(username=user,product_name=product.product_name)
    wishListProcuct.delete()
    return redirect('/shop/wishlist')

def orders(request):
    orders = OrderDetails.objects.filter(username=request.user.username)
    len1 = len(orders)
    if len1==0:
        return render(request,'orders.html',{'orders':None})
    return render(request,'orders.html',{'orders':orders,'len1':len1})

def orderCancel(request,name):
    order = OrderDetails.objects.get(product_name=name)
    order.delete()
    messages.info(request,'Order Cancelled')
    return redirect('/shop/order')