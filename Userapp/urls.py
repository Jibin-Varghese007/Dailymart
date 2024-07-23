from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
  path('vegefruti',views.vegefruti, name='vegefruti'),
  path('categorycards',views.categorycards, name='categorycards'),
  path('singlecategory/<int:id>',views.singlecategory, name='singlecategory'),
  path('productcards/<str:category>',views.productcards, name='productcards'),
  path('singleproduct/<int:id>',views.singleproduct, name='singleproduct'),
  path('tempcontact',views.tempcontact, name='tempcontact'),
  path('contform',views.contform,name='contform'),
  path('contactfruti_data',views.contactfruti_data,name='contactfruti_data'),
  path('formlogin',views.formlogin,name='formlogin'),
  path('registerform',views.registerform,name='registerform'),
  path('Registerfruit_data',views.Registerfruit_data,name='Registerfruit_data'),
  path('userlogout',views.userlogout,name='userlogout'),
  path('publicdata',views.publicdata,name='publicdata'),
  path('cart',views.cart,name='cart'),
  path('checkout',views.checkout,name='checkout'),
  path('About',views.About,name='About'),
  path('cartdata/<int:id>',views.cartdata,name='cartdata'),
  path('deletecart/<int:id>', views.deletecart , name='deletecart'),
  path('checkoutdata',views.checkoutdata,name='checkoutdata'),
  path('success',views.success,name='success'),
]