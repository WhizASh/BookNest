from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Items(models.Model):
    category =  models.ForeignKey(Category,related_name="items",on_delete=models.CASCADE)
    publication = models.CharField(max_length=30)
    is_combo = models.BooleanField(default=False)
    book_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    #image will be saved to uplode image path inside the media_ROOT path folder 
    image = models.ImageField(upload_to="item_images",blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User ,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book_name
    
