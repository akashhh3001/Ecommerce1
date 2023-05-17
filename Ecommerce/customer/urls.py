from django.urls import path
from customer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   # path("/",views.View.as_view(),name="homeview"),
   path("register/",views.SignupView.as_view(),name="signup"),
   path("",views.SignInView.as_view(),name="signin"),
   path("basee/",views.indexView.as_view(),name="base"),
   path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
   path("products/<int:id>/carts/add/",views.AddCartView.as_view(),name="cart-add"),
   path("customer/carts/all",views.CartListView.as_view(),name="cart-list"),
   path("carts/<int:id>/change/",views.CartRemoveView.as_view(),name="cart-change"),
   path("orders/add/<int:id>",views.MakeOrderView.as_view(),name="create-order"),
   path("orders/list",views.OrderView.as_view(),name="order-list"),
   path("orders/<int:id>/cancel/",views.CancelOrder.as_view(),name="cancelled"),
   path("offers/all",views.DiscountProductsView.as_view(),name="offers"),
   path("review/<int:id>/all",views.ReviewCreateView.as_view(),name="review-add"),
   path("logout",views.sign_view,name="signout"),
   # path("home",views.i)



]
