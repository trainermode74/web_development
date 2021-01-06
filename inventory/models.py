from django.db import models

# Create your models here.

class Device(models.Model):

    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()

    choice = (
        ("AVAILABLE", "Item ready to be purchased"),
        ("SOLD", "Item sold"),
        ("RESTOCKING", "Item restocking in few days")
    )

    status = models.CharField(max_length=10, choices=choice, default="SOLD")
    issues = models.CharField(max_length=100, default="No issues")

    class Meta:
        abstract = True


    def __str__(self):
        return 'Type : {0} Price {1}'.format(self.type, self.price)

class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass

