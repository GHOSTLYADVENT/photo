from django.db import models
import uuid
#from django.contrib.auth.models import User


class Photo(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
#    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    category = models.ManyToManyField('Category')
    image = models.ImageField(upload_to='new_img')



class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
