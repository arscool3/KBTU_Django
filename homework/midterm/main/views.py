from django.shortcuts import render,redirect
from .models import Product,Basket,In_Basket,Order,In_Order
from django.contrib.auth.decorators import login_required
# Create your views here.
def main(request):
	products =Product.objects.all()
	if request.user.is_authenticated:
		try:
			basket =Basket.objects.get(user=request.user)
		except:
			basketcr = Basket()
			basketcr.user =request.user
			basketcr.save()

	return render(request,"home.html",{'products':products})
@login_required
def add(request,product_id):
	product =Product.objects.get(id=product_id)
	basket = Basket.objects.get(user=request.user)
	try:
		basket_in_q = In_Basket.objects.get(product=product)
		basket_in_q.quantity+=1
		basket_in_q.save()
	except:
		add_to_basket = In_Basket()
		add_to_basket.basket=basket
		add_to_basket.prodcut=product
		add_to_basket.save()
	return redirect("cart")
@login_required
def cart(request):
	basket =Basket.objects.get(user=request.user)
	items = In_Basket.objects.filter(basket=basket)
	return render(request,'cart.html',{'items':items,"basket":basket})
@login_required
def increase(request,cart_id,product_id):
	basket = Basket.objects.get(id=cart_id)
	in_bask = In_Basket.objects.filter(basket=basket)
	prod = Product.objects.get(id=product_id)
	product = in_bask.get(prodcut=prod)
	product.quantity+=1
	product.save()
	return redirect('cart')
@login_required
def decrease(request,cart_id,product_id):
	basket = Basket.objects.get(id=cart_id)
	in_bask = In_Basket.objects.filter(basket=basket)
	prod = Product.objects.get(id=product_id)
	product = in_bask.get(prodcut=prod)
	product.quantity-=1
	product.save()
	return redirect('cart')
@login_required
def checkout(request):
	order=Order()
	order.user = request.user
	order.save()
	order_last = Order.objects.filter(user=request.user).order_by('-id').first()
	return redirect('checkoutcont',order_id=order_last.id)

def check_continue(request,order_id):
	basket = Basket.objects.get(user=request.user)
	basket_items = In_Basket.objects.filter(basket=basket)
	for basket_item in basket_items:
		order_item = In_Order()
		order_item.order=Order.objects.get(id=order_id)
		order_item.prodcut = basket_item.prodcut
		order_item.quantity = basket_item.quantity
		order_item.save()
		basket_item.delete()
	order = Order.objects.get(id=order_id)
	order_items = In_Order.objects.filter(order=order)
	return render(request,"checkout.html",{"order_items":order_items})

def orders_list(request):
	orders = Order.objects.filter(user=request.user)
	return render(request,"order_list.html",{"orders":orders})

def order_detail(request,order_id):
	order = Order.objects.get(id=order_id)
	order_object  = In_Order.objects.filter(order=order)
	return render(request,"order_detail.html",{'order_objects':order_object})

@login_required
def product_details(request,product_id):
	product =Product.objects.get(id=product_id)
	return render(request, 'product_details.html', {'product': product})