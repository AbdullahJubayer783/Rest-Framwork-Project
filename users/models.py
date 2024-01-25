from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="users/images/")
    mobile_no = models.IntegerField()

    def __str__(self):
        return f'{self.user.first_name}'