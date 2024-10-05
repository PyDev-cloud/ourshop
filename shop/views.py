from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.db.models.functions import Random
from django.views.generic import *;
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

class BaseContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Subcategory"] = Subcategory.objects.all()
        context["Categories"] = Category.objects.all()
        return context
    

class Home(BaseContextMixin,TemplateView):
    template_name="shop/Home.html"
    
    def get_context_data(self, **kwargs) :
        
        context = super().get_context_data(**kwargs)
        
        context["sliderItem"]=SliderItem.objects.all()
        context["products"]=Product.objects.order_by(Random())
        context["f_product"]=Product.objects.filter(feature=True)
        return context
    

class DetailsProduct(BaseContextMixin,DetailView):
    model=Product
    template_name="shop/ProductDetails.html"
    pk_url_kwarg="pk"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_product"]=self.get_object().related
        return context


class AddCart(View):
    def post(self,request,*args, **kwargs):
        product=get_object_or_404(Product,id=kwargs.get("pk"))
        user=request.user
        Cart.objects.create(user=user, product=product)       
        return redirect ("/Viwcart");
    

class Show_Cart(TemplateView):
    template_name="shop/Cart.html"

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            user=request.user
            cart=Cart.objects.filter(user=user)
            amount=0
            shipping_amount=100
            
            for cart_item in cart:
                total = cart_item.quantity * cart_item.product.discount_price
                totalamount=total
                amount += total
               
                total_amount = amount + shipping_amount
            context = {
            "cart": cart,
            "tal":totalamount,
            "amount": amount,
            "shipping_amount": shipping_amount,
            "total_amount": total_amount,
            }
        
            return render(request, "shop/Cart.html", context)
    
        return render(request, "shop/Cart.html", {"cart": []})
        


   
    

class Checkout(TemplateView):
    template_name="shop/checkout.html"



    
def plus(request):
        if request.method == "GET":
            prod_id = request.GET.get("prod_id")
            cart_item = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            cart_item.quantity += 1
        
            cart_item.save()

            amount = 0
            shipping_amount = 100
            
            # Calculate total amount for all cart items
            cart_items = Cart.objects.filter(user=request.user)
            for item in cart_items:
                total = item.quantity * item.product.discount_price
                amount += total
                
                total_amount = amount + shipping_amount
            
            data = {
                'quantity': cart_item.quantity,
                'amount': amount,
                'totalamount': total_amount,
                
            }
            return JsonResponse(data)

def Minus(request):
    prod_id=request.GET["prod_id"]
    c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
    c.quantity-=1
    c.save()
    amount = 0
    shipping_amount = 100
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        total=item.quantity * item.product.discount_price
        amount +=total
        total_amount = amount + shipping_amount
    data={
            "quantity":c.quantity,
            "amount":amount,
            "totalamount":total_amount
        }

    return JsonResponse(data);


def remove(request):
    prod_id=request.GET.get("prod_id")
    c=Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
    c.delete()
   
    amount = 0
   
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        total=item.quantity * item.product.discount_price
        amount +=total
        
    data={
            "quantity":c.quantity,
            "amount":amount,
            
        }

    return JsonResponse(data);

    
    
    
    