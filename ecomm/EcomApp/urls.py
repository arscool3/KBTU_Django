from django.urls import path
from . import views
from .views import SpecificView
urlpatterns = [
    path("",views.index,name="index"),
    path("prodSpecfic/<int:pk>/",SpecificView.as_view(),name="prodSpecfic"),
    path("mobileView/",views.mobileView,name="mobileView"),
    path("laptopView/",views.mlaptopView,name="laptopView"),
    path("tvView/",views.tvView,name="tvView"),
    path("rangeView/",views.rangeView,name="rangeView"),
    path('sortAsc/',views.sortProducts,name="sortAsc"),
    path('search/',views.search,name="search"),
    path("addCart/<int:prod_id>",views.addCart,name="addCart"),
    path("viewCart/",views.viewCart,name="viewCart"),
    path("updateqty/<int:uval>/<int:item_id>/",views.updateqty,name="updateqty"),
    path("removeCart/<int:item_id>/",views.remove_from_cart,name="removeCart"),
    path('register/',views.register,name="register"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("placeOrder/",views.placeOrder,name="placeOrder"),
    path("payment/",views.makePayment,name="payment"),
    path("viewOrder/",views.viewOrder,name="viewOrder"),
    path("address/",views.genAddress,name="address"),
    path("addAddress/",views.addAddress,name="addAddress"),
    path("update_address/<pid>",views.updateAddress,name="update_address"),
    path("delete_address/<pid>",views.deleteAddress,name="delete_address"),
    #path("sendMail/",views.sendUserMail,name="sendMail"),
    path("buy/<int:prod_id>",views.buy,name="buy"),
]
