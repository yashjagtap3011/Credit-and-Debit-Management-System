from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
class Transaction(models.Model):
 class Type(models.TextChoices):
  CREDIT="credit","Credit"
  DEBIT="debit","Debit"
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="transactions")
 transaction_type=models.CharField(max_length=6,choices=Type.choices)
 amount=models.DecimalField(max_digits=12,decimal_places=2)
 description=models.CharField(max_length=200)
 category=models.CharField(max_length=80)
 date=models.DateField()
 created_at=models.DateTimeField(auto_now_add=True)
 updated_at=models.DateTimeField(auto_now=True)
 class Meta: ordering=["-date","-created_at"]
 def __str__(self): return f"{self.get_transaction_type_display()} {self.amount} ? {self.user}"
class Tutorial(models.Model):
 title=models.CharField(max_length=160)
 slug=models.SlugField(unique=True,blank=True)
 description=models.CharField(max_length=300)
 content=models.TextField()
 image=models.ImageField(upload_to="tutorials/",blank=True)
 category=models.CharField(max_length=80)
 created_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name="tutorials")
 created_at=models.DateTimeField(auto_now_add=True)
 updated_at=models.DateTimeField(auto_now=True)
 is_published=models.BooleanField(default=False)
 class Meta: ordering=["title"]
 def save(self,*args,**kwargs):
  if not self.slug: self.slug=slugify(self.title)
  super().save(*args,**kwargs)
 def get_absolute_url(self): return reverse("tutorial_detail",kwargs={"slug":self.slug})
 def __str__(self): return self.title
