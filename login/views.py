from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Profile
from product.models import Product,CartProducts
from checkout.models import OrderDetails
from .forms import ProfileForm,UserForm,ProductForm,ProductForms
from django.contrib import messages

# Create your views here.
def home(request):
    user1 = request.user.username
    products = CartProducts.objects.filter(username=user1)
    len1 = len(products)
    if len1 == 0:
        len1 = ''
    return render(request,'home.html',{'len':len1})

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user_name = request.POST['username']
        password_ = request.POST['password']
        user = auth.authenticate(username=user_name,password=password_)
        if user is not None:
            auth.login(request,user)
            superUsers = User.objects.filter(is_superuser=True)
            loginUser = User.objects.get(username=user_name)
            if loginUser in superUsers:
                return redirect('/adminpanel/') 
            return redirect('/')
        else:
            messages.info(request,"Invalid Login Details..!!!")
            return redirect('.')
    else:
        return render(request,'login.html',{})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email_ = request.POST['email']
        contact_number_ = request.POST['ph-no']
        # birthdate_ = request.POST['bday']
        password_ = request.POST['password']
        repassword_ = request.POST['repassword']

        if password_ == repassword_:
            if User.objects.filter(email=email_).exists():
                messages.info(request,'Email Already Exist..!!')
                return redirect('.')
            elif Profile.objects.filter(contact_number=contact_number_).exists():
                messages.info(request,'Contact number Already Exist..!!')
                return redirect('.')
            elif len(password_) < 8:
                messages.info(request,'Password must have more than 8 characters..!!')
                return redirect('.')
            else:
                user = User.objects.create_user(first_name=first_name,password=password_,last_name=last_name,username=user_name,email=email_)
                profile = Profile(user=user,contact_number=contact_number_)
                profile.save()
                print(profile);
                user.save()
                auth.login(request,user)
        else:
            messages.info(request,"Passwords didn't match..!!")
            return redirect('.')
        # users = Users(firstname=first_name,password=password_,lastname=last_name,username=user_name,email=email_,birthdate=birthdate_,contact_number=contact_number_)
        # users.save()
        return redirect('/')
        # users = UsersForm(request.POST or None)
        # print(users)
        # print(users.is_valid())
        # if users.is_valid():
        #     print('hj')
        #     users.save()
        #     users = UsersForm()
    else:
        return render(request,'signup.html',{})

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    # if request.method == 'POST':
    #     u_form = UserForm(request.POST,instance=request.user)
    #     p_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)

    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         return redirect('./')
    # else:
    #     u_form = UserForm(instance=request.user)
    #     p_form = ProfileForm(instance=request.user.profile)

    # context = {
    #     'user' : u_form,
    #     'profile' : p_form
    # }
    # return render(request,'profile.html',context)
    if request.method == 'POST':
        current = request.user.username
        print(current)
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email_ = request.POST['email']
        contact_number_ = request.POST['ph-no']
        # birthdate_ = request.POST['bday']

        p_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()

        user = User.objects.filter(username=current).first()
        user.username = user_name
        user.first_name = first_name
        user.last_name = last_name
        user.email = email_
        # user.profile.birthdate = birthdate_
        user.profile.contact_number = contact_number_
        
        print(user.profile.image.url)
        # print(user.first_name)
        user.save()
        user.profile.save()
        messages.info(request,'Profile successfully updated.')
        return redirect('./')
    else:
        current = request.user.username
        print(current)
        p_form = ProfileForm(instance=request.user.profile)
        #p_form.save()
        # users = Profile()
        # context = {
        #     'username':users.user.username,
        # }
        return render(request,'profile.html',{'pic':p_form})

def a(request):
    return render(request,'base.html',{})

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        products = Product.objects.all()
        list_ = []
        for product in products:
            if search.lower() in product.product_name.lower():
                list_.append(product)
    return render(request,'shop.html',{'products':list_})

def changepassword(request):
    if request.method == "POST":
        old = request.POST['old']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user = User.objects.get(username=request.user.username)
        print(old,pass1,pass2,user,user.password)
        user.set_password(pass1)
        if old == user.password:
            print('1')
            if pass1==pass2:
                print('2')
                user.password = pass1
                user.save()
                return render('/')
    return render(request,'changepassword.html',{})

def adminpanel(request):
    flag = request.user in User.objects.filter(is_superuser=True)
    if flag == True:
        products = Product.objects.all()
        len1 = len(products)
        form = ProductForm()
        orders = OrderDetails.objects.all()
        len2 = len(orders)
        if len2==0:
            return render(request,'adminpanel.html',{'products':products,'len':len1,'form':form,'orders':None,'len2':len2})
        list1 = []
        # for order in orders:
        #     list1.append(Product.objects.get(product_name=order.product_name).img1.url)
        return render(request,'adminpanel.html',{'products':products,'len':len1,'form':form,'orders':orders,'len2':len2})
    return redirect('/')

def addproduct(request):
    if request.method == 'POST':
        # product_id = request.POST['id']
        # product_number = request.POST['productnum']
        # product_name = request.POST['productname']
        # catagory = request.POST['catagory']
        # sub_catagory = request.POST['sub-catagory']
        # stock = request.POST['stock']
        # price = request.POST['price']
        # img1 = f"product_pics/{request.POST['image1']}"
        
        p_form = ProductForm(request.POST,request.FILES)
        
        if p_form.is_valid():
            p_form.save()

        # print(product_id,product_name,product_number,catagory,sub_catagory,stock,price,img1)
        # product = Product(product_id=product_id,product_name=product_name,product_number=product_number,catagory=catagory,sub_catagory=sub_catagory,stock=stock,price=price,img1=img1)
        # product.save()
        
    return redirect('/adminpanel')

def removeProduct(request,name):
    product = Product.objects.get(product_name=name)
    product.delete()
    return redirect('/adminpanel')

def editProduct(request,name):
    # product = Product.objects.get(product_name=name)
    # if request.method == 'POST':
    #     product_name = request.POST['product_name']
    #     # catagory = request.POST['catagory']
    #     # sub_catagory = request.POST['sub-catagory']
    #     # stock = request.POST['stock']
    #     # price = request.POST['price']

    #     # product.product_name = product_name
    #     # product.catagory = catagory
    #     # product.sub_catagory = sub_catagory
    #     # product.stock = stock
    #     # product.price = price
    #     # product.save()

    #     form = ProductForms(request.POST,request.FILES,instance=product)
    #     if form.is_valid():
    #         form.save()
    #         messages.info(request,'Product successfully updated')
    #         name = product_name
    # else:
    product = Product.objects.get(product_name=name)
    form = ProductForms(instance=product)
    
    return render(request,'editProduct.html',{'form':form,'product':product})

def editProductPost(request,name):
    product = Product.objects.get(product_name=name)
    if request.method == 'POST':
        product_name = request.POST['product_name']

        form = ProductForms(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            messages.info(request,'Product successfully updated')
            name = product_name
    return redirect(f'/adminpanel/edit/{name}')