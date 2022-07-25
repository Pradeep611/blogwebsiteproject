from django.db import models
from django.utils.timezone import now
from adminapp.models import subcategory
# Create your models here.



class contacts(models.Model):
    uname = models.CharField(max_length=30)
    mobno = models.IntegerField()
    email = models.EmailField()
    udesc = models.CharField(max_length=1000)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.uname, self.email)

class Register(models.Model):
    unm = models.CharField(max_length=30)
    mno = models.IntegerField()
    eid = models.EmailField()
    pwd = models.CharField(max_length=30)
    status = models.CharField(max_length=10,default='No')
    regdate = models.DateField()

    def __str__(self):
        return "%s" % (self.unm)



class Blog(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    bl_image = models.ImageField(upload_to = 'userapp/blog/images',default="")
    slug = models.CharField(max_length=130)
    unm = models.ForeignKey(Register, on_delete = models.CASCADE)
    subcategory = models.ForeignKey(subcategory, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(now)

    
    