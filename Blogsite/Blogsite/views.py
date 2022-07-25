from django.shortcuts import render
from userapp import views
from userapp.models import contacts
from django.contrib import messages
from adminapp.models import *

# def index(request):
#     rec = request.session.get('sessid',False)
#     context = {'rec':rec}
#     return render(request,'userapp/userbluhome.html',context)

def landingpage(request):
    return render(request,'landing.html')

def about(request):
    return render(request,'about.html')

def blogs(request):
    return render(request,'blogs.html')

def contact(request):
    rec = request.session.get('sessid',False)
    context = {'rec':rec}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']

        if name and email and phone and msg:

         data = contacts(uname=name,mobno=phone,email=email,udesc=msg)
         data.save()
         messages.success(request, 'your messages has been sent successfully')

        else:
            messages.error(request, 'Please fill the details correctly')
    return render(request,'contact.html',context)

    
def showcategorycommon(request):
    category_data = category.objects.all()
    rec = request.session.get('sessid',False)
    print('showcategorycommon  ' ,rec)
    context = {'category_data':category_data,'rec':rec}

    return render(request,'categoryshowcommon.html',context)
  

def subcategorycom(request):
    
    subcategory_data = subcategory.objects.all()
    rec = request.session.get('sessid',False)
    context = {'subcategory_data':subcategory_data,'rec':rec}
    


    return render(request,'subcategorycom.html',context)

def subshow(request,cname):
    data = subcategory.objects.filter(cname=cname)
    rec = request.session.get('sessid',False)
    context = {'data':data,'rec':rec}
    return render(request,'subshow.html',context)

