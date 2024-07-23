from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import*
from Adminapp.models import*
from django.db.models.aggregates import Sum
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def vegefruti(request): 
  data = Dailycategory.objects.all()
  data1 = Products.objects.all()
  return render(request,"vegefruti.html",{'data':data, 'data1':data1})
  

def categorycards(request):
  data = Dailycategory.objects.all()
  return render(request,'categorycards.html',{'data':data})

def singlecategory(request,id):
    data =  Dailycategory.objects.filter(id=id)
    return render(request,"singlecategory.html",{'data' : data})

def productcards(request,category):
  if(category == "all"):
   data = Products.objects.all()
  else:
   data = Products.objects.filter(Productcategory=category)
  data1 = Dailycategory.objects.all()
  return render(request,'productcards.html',{'data':data, 'data1':data1})

def singleproduct(request,id):
    data =  Products.objects.filter(id=id)
    return render(request,"singleproduct.html",{'data' : data})

def tempcontact(request):
  return render(request,'tempcontact.html')

def contform(request):
    return render(request,"contform.html")

def contactfruti_data(request):
  if request.method == "POST":
   ContactName  = request.POST['name']
   ContactNumber = request.POST['number']
   EmailId = request.POST['email']
   Message = request.POST['message']
   data = vegecontact(ContactName= ContactName,ContactNumber=ContactNumber,EmailId=EmailId,Message=Message)
  data.save()
  return redirect('contform')


def registerform(request):
    return render(request,"registerform.html")

def Registerfruit_data(request):
  if request.method == "POST":
   UserName = request.POST['username']
   Password = request.POST['password']
   EmailId = request.POST['email']
   Phonenumber = request.POST['number']
   data = Fruitregister(UserName=UserName,Password=Password,EmailId=EmailId,Phonenumber=Phonenumber)
   data.save()
  return redirect('registerform')


def formlogin(request):
    return render(request,"formlogin.html")

def publicdata(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        if Fruitregister.objects.filter(UserName=username,Password=password).exists():
           data = Fruitregister.objects.filter(UserName=username,Password=password).values('id','Phonenumber','EmailId').first()
           
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['Phonenumber'] 
           request.session['email_u'] = data['EmailId'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('vegefruti') 
        else:
            return render(request,'formlogin.html',{'msg':'invalid user credentials'})
    else:
        return redirect('formlogin')

def userlogout(request):
    
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('formlogin')


def About(request):
    return render(request,"About.html")


def cart(request):
    c = request.session.get('u_id')
    data = Cart.objects.filter(cartuser=c,status=0)
    a = Cart.objects.filter(cartuser=c,status=0).aggregate(Sum('total'))
    return render(request,"cart.html",{'data':data, 'a':a})


def cartdata(request,id):
   if request.method == "POST":
      user_id = request.session.get('u_id')
      quantity = request.POST['quantity']
      total = request.POST['total']
      data = Cart(cartuser=Fruitregister.objects.get(id=user_id), cartproduct=Products.objects.get(id=id),quantity=quantity,total=total)
      data.save()
   return redirect('cart')


def deletecart(request,id):
  Cart.objects.filter(id=id).delete()
  return redirect('cart')

def checkout(request):
    c = request.session.get('u_id')
    data = Cart.objects.filter(cartuser=c,status=0)
    b = Cart.objects.filter(cartuser=c,status=0).aggregate(Sum('total'))
    return render(request,"checkout.html",{'data':data, 'b':b})

def checkoutdata(request):
   if request.method=="POST":
       checkoutid = request.session.get('u_id')
       address = request.POST.get('address')
       city = request.POST.get('city')
       country = request.POST.get('country')
       pincode = request.POST.get('pincode')
       
       buy = Cart.objects.filter(cartuser=checkoutid,status=0)
       
       for i in buy :
          data = Checkout(usercheckout=Fruitregister.objects.get(id=checkoutid), checkoutcart=Cart.objects.get(id=i.id), address=address,city=city, country=country, postcode=pincode)
          data.save()
          Cart.objects.filter(id=i.id).update(status=1)
       return redirect('success')
   
def success(request):
  s = request.session.get('u_id')
  data= Checkout.objects.filter(usercheckout=s)
  return render (request,'success.html',{'data':data})