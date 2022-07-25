from django.db import models

# Create your models here.
class category(models.Model):
    catname = models.CharField(max_length=30)
    caticon = models.ImageField(upload_to = 'adminapp/images/',default="")
    catdesc = models.CharField(max_length=2000)
    regdate = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.catname
    

class subcategory(models.Model):
    scatname = models.CharField(max_length=30)
    scicon = models.ImageField(upload_to = 'adminapp/images',default="")
    scdesc = models.CharField(max_length=2000)
    regdate = models.DateField()
    cname = models.ForeignKey(category,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.scatname

class Regadmin(models.Model):
    email = models.EmailField(primary_key=True)
    adpass = models.CharField(max_length=15)
   
    regdate = models.DateField()