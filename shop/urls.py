
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
  path("",Home.as_view(),name="home"),
  path("DetailsProduct/<int:pk>/",DetailsProduct.as_view(),name="DetailsProduct"),
  path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
  path('category/<int:category_id>/subcategory/<int:subcategory_id>/', CategoryView.as_view(), name='subcategory'),
  path("Viwcart/",Show_Cart.as_view(),name="Viewcart"),
  path("cart/<int:pk>/",AddCart.as_view(),name="cart"),
  path("checkout/",Checkout.as_view(),name="checkout"),
  path("pluscart/",view=plus),
  path("minuscart/",view=Minus),
  path("removecart/",view=remove),
  path("shop/",shop.as_view(),name="shop"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
