from django.db import models
from users.models import UserModel
# Create your models here.
class ColorCategoryModel(models.Model):
    name = models.CharField(max_length = 20)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    def __str__(self):
        return f"Color{self.name}"
    
class FlowerCategoryModel(models.Model):
    name = models.CharField(max_length = 20)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    def __str__(self):
        return f"Color{self.name}"
    
class FlowerModel(models.Model):
    image = models.ImageField(upload_to="flower/images/",blank=True,null=True)
    title = models.CharField(max_length=40)
    descriptions = models.TextField()
    color = models.ManyToManyField(ColorCategoryModel)
    flower = models.ManyToManyField(FlowerCategoryModel)
    quantity = models.IntegerField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title
STAR_CHOICES = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class ReviewModel(models.Model):
    reviewer = models.ForeignKey(UserModel,on_delete = models.CASCADE)
    flower = models.ForeignKey(FlowerModel, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateField(auto_now_add = True)
    rating = models.CharField(choices=STAR_CHOICES,max_length=14)

    def __str__(self):
        return f"Reviewer->{self.reviewer.user.first_name} commented on->{self.flower.title}"
