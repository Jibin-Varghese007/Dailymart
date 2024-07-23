from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import*
from Userapp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def dashmin(request):
  category = Dailycategory.objects.all().count()
  product = Products.objects.all().count()
  user =  Fruitregister.objects.all().count()
  feedback = vegecontact.objects.all().count()
  orders = Checkout.objects.all().count()
  return render(request,'dashmin.html',{'category':category, 'product':product, 'user':user, 'feedback':feedback, 'orders':orders})
  

def addcategory(request):
  data = Dailycategory.objects.all()
  return render(request,'addcategory.html',{'data':data})

def dailyform(request):
  return render(request,'dailyform.html')

def categoryedit(request,id):
  data = Dailycategory.objects.filter(id=id)
  return render(request, "categoryedit.html",{"data":data})

def categoryupdate(request,id):
  if request.method == "POST":
    categoryName = request.POST['name']
    categoryDescription = request.POST['description']
    try:
            img_c = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
    except MultiValueDictKeyError:
            file = Dailycategory.objects.get(id=id).img
    Dailycategory.objects.filter(id=id).update(categoryName=categoryName,categoryDescription=categoryDescription,img=file)
  return redirect('addcategory')


def categorydelete(request,id):
  data = Dailycategory.objects.filter(id=id).delete()
  return redirect(request, "'addcategory'.html",{"data":data})

def dailycategory_data(request):
  if request.method == 'POST':
    categoryName = request.POST['name']
    categoryDescription = request.POST['description']
    img = request.FILES['images']
    data = Dailycategory(categoryName=categoryName,categoryDescription=categoryDescription, img=img)
    data.save()
    return redirect('dailyform')


def addproduct(request):
  data = Products.objects.all()
  return render(request,'addproduct.html',{'data':data})

def productform(request):
  data = Dailycategory.objects.all()
  return render(request,'productform.html',{'data':data})

def Products_data(request):
  if request.method == 'POST':
    ProductName = request.POST['pname']
    Price = request.POST['number']
    Productcategory = request.POST['name']
    img = request.FILES['image']
    data = Products(ProductName=ProductName,Price=Price,Productcategory=Productcategory, img=img)
    data.save()
    return redirect('productform')

def editproduct(request,id):
  data = Products.objects.filter(id=id)
  return render(request, "editproduct.html",{'data':data})

def updateproduct(request,id):
  if request.method == "POST":
    ProductName = request.POST['pname']
    Price = request.POST['number']
    Productcategory = request.POST['name']
    try:
            img_c = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
    except MultiValueDictKeyError:
            file = Products.objects.get(id=id).img
    Products.objects.filter(id=id).update(ProductName=ProductName,Price=Price,Productcategory=Productcategory,img=file)
  return redirect('addproduct')

def deleteproduct(request,id):
  data = Products.objects.filter(id=id).delete()
  return redirect("addproduct")


def tablecontact(request):
  data = vegecontact.objects.all()
  return render(request,'tablecontact.html',{'data':data})

def registertab(request):
  data = Fruitregister.objects.all()
  return render(request,'registertab.html',{'data':data})

def logintab(request):
  return render(request,'logintab.html')


def ordertable(request):
  data = Checkout.objects.all()
  return render(request,'ordertable.html',{'data':data})



