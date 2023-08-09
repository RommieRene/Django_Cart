from django.shortcuts import render
from .models import Cart, Category, Product, Contact
# Create your views here.

def home(request):
    category_list=Category.objects.all()
    cart_list = Cart.objects.all()
    return render(request,'main/home.html',context={
        'category_list':category_list,
        'cart_list':cart_list
    })
def cart(request):
    cart_list = Cart.objects.all()
    return render(request,'main/cart.html',context={
        'cart_list':cart_list
    })
def prod(request):
    prod_list = Product.object.all()
    return render(request,'main.product.html',context={
        'prod_list':prod_list
    })
def add_to_cart(request):
    if request.method =='POST':
        prod_id=request.POST.get('prod_id')
        my_prod=request.POST.get(id=prod_id)
        Cart.objects.create(product=my_prod)
    return redirect('home')
def delete_to_cart(request):
    if request.method =='POST':
        prod_id=request.POST.get('prod_id')
        Cart.objects.create(product=my_prod)

    return redirect('cart')