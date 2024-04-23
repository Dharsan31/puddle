from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=200)
    class Meta:
        ordering=('name',)
        verbose_name_plural="Categories"
    def __str__(self):
        return self.name

class Item(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    description=models.TextField(null=True,blank=True)
    price=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_sold=models.BooleanField(default=False)
    image=models.ImageField(upload_to="item_images",blank=True,null=True)
    created_by=models.ForeignKey(User,related_name="items",on_delete=models.CASCADE)
    def __str__(self):
        return self.name 