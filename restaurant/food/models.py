from django.db import models

class Restaurant(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone = models.TextField()

    def __str__(self):
        return str(self.id)
  
class Purchase(models.Model):
    date= models.TextField()
    identification= models.TextField()
    payment = models.TextField()
    service = models.TextField()
    restaurant = models.ForeignKey(
        "Restaurant", on_delete=models.CASCADE
    )
    def __str__(self):
        return str(self.id)

class Dish(models.Model):
    purchase = models.ForeignKey(
        "Purchase", on_delete=models.CASCADE
    )
    def __str__(self):
        return str(self.id)

class Detaildish(models.Model):
    name = models.TextField()
    size = models.BigIntegerField()
    price = models.BigIntegerField()
    dish = models.ForeignKey(
        "Dish", on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title

