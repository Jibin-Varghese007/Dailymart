from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
    path('dashmin',views.dashmin, name='dashmin'),
    path('addcategory',views.addcategory, name='addcategory'),
    path('dailycategory_data',views.dailycategory_data, name='dailycategory_data'),
    path('dailyform',views.dailyform, name='dailyform'),
    path('categoryedit/<int:id>', views.categoryedit , name='categoryedit'),
    path('categoryupdate/<int:id>', views.categoryupdate , name='categoryupdate'),
    path('categorydelete/<int:id>', views.categorydelete , name='categorydelete'),
    path('addproduct',views.addproduct, name='addproduct'),
    path('productform',views.productform, name='productform'),
    path('Products_data',views.Products_data, name='Products_data'),
    path('editproduct/<int:id>', views.editproduct , name='editproduct'),
    path('updateproduct/<int:id>', views.updateproduct , name='updateproduct'),
    path('deleteproduct/<int:id>', views.deleteproduct , name='deleteproduct'),
    path('tablecontact',views.tablecontact, name='tablecontact'),
    path('logintab',views.logintab, name='logintab'),
    path('registertab',views.registertab, name='registertab'),
    path('ordertable',views.ordertable, name='ordertable'),
   


]