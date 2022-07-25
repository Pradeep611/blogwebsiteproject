from django.shortcuts import render,redirect
from adminapp.models import category,subcategory,Regadmin
from userapp.models import contacts,Register,Blog
from datetime import date
from django.contrib import messages


# Create your views here.
def index(request):
    ad_rec = request.session.get('sessidad',False)
    context = {'ad_rec':ad_rec}
   
    return render(request,'adminapp/index.html',context)
    
def adminlogin(request):
    if request.method == "POST":
        adminemail = request.POST['adminemail']
        adminpass = request.POST['adminpass']

        data = Regadmin.objects.filter(email=adminemail,adpass=adminpass)
        if data:
            messages.success(request,'You are logged in successfully')
            request.session['sessidad'] = adminemail
            
            return redirect('/adminapp')
    
    return render(reqeuest,'adminapp/base.html')

def adminlogout(request):
    del request.session['sessidad']
    return redirect('/adminapp')

def categoryadd(request):

    ad_rec = request.session.get('sessidad',False)
    print(ad_rec)

    if ad_rec == False:
        return redirect('/adminapp')

    else:

        if request.method=="POST":
            cname = request.POST['cname']
            cicon = request.FILES.get('cicon')
            cdesc = request.POST['cdesc']   
            
            if cname and cdesc:

                data = category(catname=cname,caticon=cicon,catdesc=cdesc)
                data.save()
                messages.success(request, 'Category has been added successfully')
            
        context = {'ad_rec':ad_rec}
        return render(request,'adminapp/categoryadd.html',context)

    




def categoryshow(request):
    data = category.objects.all()

    return render(request,'adminapp/categoryshow.html',{'data':data})

def categoryupdate(request,c_id):

    data = category.objects.get(id=c_id)

    if request.method == "POST":
        cname = request.POST['cname']
        cicon = request.FILES.get('cicon',default='')
        cdesc = request.POST['cdesc']

        if cname and cdesc:
         category.objects.filter(id = c_id).update(catname=cname,caticon=cicon,catdesc=cdesc)
         messages.success(request,'Category has been updated')

        return redirect('/adminapp/categoryshow')

    context = {'data':data}

    return render(request,'adminapp/categoryupdate.html',context)

def categorydelete(request):
    cname = request.GET.get('cname')
    
    category.objects.filter(catname=cname).delete()
    messages.error(request, 'A category has been deleted')
    
    return redirect('/adminapp/categoryshow/')
    
   
    

def subcategoryadd(request):

    data = category.objects.all()
    
    

    if request.method == "POST":
       name = request.POST['name']
       cname = category.objects.get(catname=name)
       scname = request.POST['scname']
       scicon = request.FILES['scicon']
       scdesc = request.POST['scdesc']
       regdate = date.today()

      

       data1 = subcategory(cname=cname,scatname=scname,scicon=scicon,scdesc=scdesc,regdate=regdate)
       data1.save()
       messages.success(request,'Subcategory has been added successfully')
       
    context = {'data':data}
    return render(request,'adminapp/subcategoryadd.html',context)

def subcategoryshow(request):
    data = subcategory.objects.all()
    context = {'data':data}

    return render(request,'adminapp/subcategoryshow.html',context)

def subcategoryupdate(request,sc_id):

    data = subcategory.objects.get(id = sc_id)
    context = {'data':data}

    if request.method == "POST":
        cname = request.POST['cname']
        scname = request.POST['scname']
        scicon = request.FILES['scicon']
        scdesc = request.POST['scdesc']

        subcategory.objects.filter(id= sc_id).update(scatname=scname,scicon=scicon,scdesc=scdesc)
        return redirect('/adminapp/subcategoryshow')
    return render(request, 'adminapp/subcategoryupdate.html',context)

def subcategorydel(request,scat_id):
     subcategory.objects.filter(id=scat_id).delete()

     return redirect('/adminapp/subcategoryshow')

    
    
def showcontacts(request):
    data = contacts.objects.all()


    return render(request,'adminapp/showcontacts.html',{'data':data})

def showblogs(request):

    blog_data = Blog.objects.all()
    context = {'blog_data':blog_data}
     
    return render(request,'adminapp/showblogs.html',context)


def showsingle(request,slug):
    blg_data = Blog.objects.filter(slug=slug).first()

    context = {'blg_data' : blg_data}

    return render(request,'adminapp/showsingleblog.html',context)

def deleteblog(request,bl_id):
    Blog.objects.filter(id = bl_id).delete()
    messages.error(request, 'A blog has been deleted')
    return redirect('/adminapp/showblogs/')

def showusers(request):

    user_data = Register.objects.all()
    context = {'user_data':user_data}

    return render(request,'adminapp/showusers.html',context)


def search(request):

    ad_rec = request.session.get('sessidad',False)
    data = Blog.objects.filter()

    query = request.GET.get('query')
    
    blogtitle = Blog.objects.filter(title__icontains = query)
    blogcontent = Blog.objects.filter(content__icontains = query)
    allposts = blogtitle.union(blogcontent)


    context = {'ad_rec':ad_rec,'allposts':allposts,'query':query}

    return render(request,'adminapp/search.html',context)