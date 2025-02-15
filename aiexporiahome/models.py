from django.db import models

# Create your models here.
from django.db import models

class AI(models.Model):
    name= models.CharField(max_length=255,default="error 404")
    description = models.TextField(default="error 404")
    category=models.TextField(default="error 404")
    image = models.ImageField(upload_to='images/',default="error 404")
    url=models.URLField( max_length=200,default="error 404")


    def __str__(self):
        return self.name
class blog(models.Model):
    title=models.CharField(max_length=255,default="Eroor 404")
    imagee=models.ImageField( upload_to='images/',default="error 404")
    descrip=models.TextField(default="error 404")
    def __str__(self):
        return self.title
class indianAI(models.Model):
    name= models.CharField(max_length=255,default="error 404")
    description = models.TextField(default="error 404")
    category=models.TextField(default="error 404")
    image = models.ImageField(upload_to='images/',default="error 404")
    url=models.URLField( max_length=200,default="error 404")

    def __str__(self):
        return self.name
