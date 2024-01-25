from django.db import models
from users.models import UserModel
from flower.models import FlowerModel
# Create your models here.


ORDER_STATUS = [
    ('Completed','Completed'),
    ('Pending','Pending'),
]
class OrderDetails(models.Model):
    flower = models.ForeignKey(FlowerModel,on_delete=models.CASCADE)
    order_status = models.CharField(choices=ORDER_STATUS , default = 'Pending',max_length=15)
    quantity = models.IntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='histories', null=True, blank = True)
    date = models.DateTimeField(auto_now_add = True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.flower.title} Orderd By->{self.user.user.first_name}"