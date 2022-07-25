from django.shortcuts import render,redirect,HttpResponse
from userapp.models import Register,Blog
from django.contrib import messages
from adminapp.models import category,subcategory
from datetime import date

# Create your views here.

# def home(request):
#     return render(request,'userapp/userbluhome.html')

def home(request):
    rec = request.session.get('sessid',False)
    context = {'rec':rec}
    return render(request,'userapp/userbluhome.html',context)

def reguser(request):

    if request.method == "POST":
        unm = request.POST.get('unm')
        eid = request.POST.get('eid')
        mno = request.POST.get('mno')
        pwd1 = request.POST.get('pwdru1')
        pwd2 = request.POST.get('pwdru2')
        regdate = date.today()

        if pwd1 == pwd2:
            request.session['sessid'] : eid
            user_data = Register(unm=unm,mno=mno,eid=eid,pwd=pwd1,regdate=regdate)
            user_data.save()
            messages.success(request, 'you are successfully registered')
            return redirect('registered')
            

    return render(request,'userapp/userbluhome.html')


def registered(request):

    return render(request,'userapp/indexalu.html')


def login(request):

    leid = request.POST.get('leid')
    pwd1 = request.POST.get('pwdlu')

    res = Register.objects.filter(eid=leid,pwd=pwd1).exists()
    
    if res:
        request.session['sessid'] = leid
        messages.success(request, 'you are logged in successfully')
        return redirect('/userapp/login')
    else:   
       return render(request,'userapp/userbluhome.html')

def logout(request):
    del request.session['sessid']
    messages.success(request, 'You are logged out successfully')
    return redirect('/userapp/')

def contactblu(request):
    return render(request, 'userapp/contactblu.html')






def addblog(request):
    rec = request.session.get('sessid',False)
    unm = Register.objects.get(eid = rec)
    
    data = subcategory.objects.all()
    

    if request.method == "POST":
       scname = request.POST.get('scname')
       scname1 = subcategory.objects.get(scatname=scname)
       image = request.FILES.get('bgicon')
       title = request.POST['btitle']
       content = request.POST['blgcontent']
       post_date = date.today()
       slug =  scname1.scatname + '_' + scname1.scatname + '_' + title
       print(slug)
    
       blg_data = Blog(title=title,content=content,bl_image = image,slug=slug,unm=unm,subcategory=scname1,timestamp=post_date)
       blg_data.save()
       messages.success(request,'Your post has been posted successfully')

    context = {'data':data}
    return render(request,'userapp/addblog.html',context)

    


      
       

       
      

    
def addblogcat(request):
    data = category.objects.all()
    
    c_id = request.GET.get('name')
    print('not if',c_id)
    if request.method == "GET":
        print('if',c_id)
      
       

    
    context = {'data':data,'c_id':c_id}
        
    
    return render(request,'userapp/addblogcat.html',context)





def showbloghome(request):
    blog_data = Blog.objects.all()
    rec = request.session.get('sessid',False)
    context = {'blog_data':blog_data,'rec':rec}

    return render(request,'userapp/showbloghome.html',context)
    
def showblog(request,slug):
    blg_data = Blog.objects.filter(slug=slug).first()
    current_user = blg_data.unm
    rec = request.session.get('sessid',False)
    loggedin_user = Register.objects.get(unm = current_user)
    
    

    context = {'blg_data':blg_data,'rec':rec,'l_user':loggedin_user}
    
    return render(request,'userapp/showblog.html',context)


def myblogs(request):
    rec = request.session.get('sessid',False)
    unm =  Register.objects.get(eid = rec)
    user_blog = Blog.objects.filter(unm = unm)

    context = {'user_blog':user_blog}


    return render(request,'userapp/myblogs.html',context)


def updateblog(request,blg_id):

    data = Blog.objects.get(id=blg_id)
    context = {'data':data}

    if request.method == "POST":
        title = request.POST.get('btitle')
        icon = request.POST.get('bgicon')
        content = request.POST.get('blgcontent')

        Blog.objects.filter(id=blg_id).update(title=title,bl_image=icon,content=content)
        messages.success(request,'Your post has been updated successfully')

        return redirect('/userapp/showbloghome/')

    return render(request,'userapp/updateblog.html',context)


def deleteblog(request,bl_id):
    
    Blog.objects.filter(id=bl_id).delete()
    messages.error(request, 'Your post has been deleted')
    return redirect('/userapp/showbloghome')


from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string 

def success(request,email,pwed,unm):

    context = {}

    context = {'email':email}


    template = render_to_string('userapp/success.html')
        
    email = EmailMessage(

        'thanks',
        f'Hello "{unm}" Your password is {pwed} Please use this password to login ',
        settings.EMAIL_HOST_USER,
        [email]


    )

    email.fail_silently = False
    email.send()

    return HttpResponse('error please try again')

def forget_password(request):
    rec = request.session.get('sessid',False)


    if request.method == "POST":
        email1 = request.POST.get('fmail')
        if not email1:
            return HttpResponse('please ennter your email id')
        email = Register.objects.get(eid=email1)
        m_email = email.eid
        pwed = email.pwd
        unm = email.unm
        success(request,m_email,pwed,unm)
        
    return render(request,'userapp/success.html',{'rec':rec})

def search(request):

    rec = request.session.get('sessid',False)
    

    query = request.GET.get('query')
    
    blogtitle = Blog.objects.filter(title__icontains = query)
    blogcontent = Blog.objects.filter(content__icontains = query)
    allposts = blogtitle.union(blogcontent)


    context = {'rec':rec,'allposts':allposts}

    return render(request,'userapp/search.html',context)