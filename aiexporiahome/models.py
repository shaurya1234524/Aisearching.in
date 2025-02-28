from django.db import models

# Create your models here.
from django.db import models

class AI(models.Model):
    name= models.CharField(max_length=255,default="error 404")
    description = models.TextField(default="error 404")
    category=models.TextField(default="error 404")
    image = models.ImageField(upload_to='s3://shaurya-bucket-5763394/admin/img/',default="error 404")
    url=models.URLField( max_length=200,default="error 404")
    like_count = models.IntegerField(default=0)  # Store the like count

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
    like_count = models.IntegerField(default=0)  # Store the like count
    def __str__(self):
        return self.name
class AIToolRating(models.Model):
    tool = models.ForeignKey(AI, on_delete=models.CASCADE, related_name="ratings",default="Error")
    parameter = models.CharField(max_length=255,default="error")
    rating = models.IntegerField(default="error")

    def __str__(self):
        return f"{self.tool.name} - {self.parameter}: {self.rating}"

# AI Tool Advantages
class AIToolAdvantage(models.Model):
    tool = models.ForeignKey(AI, on_delete=models.CASCADE, related_name="advantages",default="error")
    text = models.TextField(default="error")

    def __str__(self):
        return f"Advantage of {self.tool.name}"

# AI Tool Disadvantages
class AIToolDisadvantage(models.Model):
    tool = models.ForeignKey(AI, on_delete=models.CASCADE, related_name="disadvantages",default="error")
    text = models.TextField(default="error")

    def __str__(self):
        return f"Disadvantage of {self.tool.name}"
class LikedAI(models.Model):
    ai_tool = models.ForeignKey(AI, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()  # Store user’s IP address
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('ai_tool', 'ip_address') 
