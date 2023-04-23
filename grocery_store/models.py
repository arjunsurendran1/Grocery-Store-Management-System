from django.db import models

# Create your models here.

class Products(models.Model):

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    status_choices = (
        ('In Stock', 'Item is in stock'),
        ('Out of Stock', 'Item is out of stock'),
    )

    status = models.CharField(max_length=50, choices=status_choices, default='In Stock')

    offer_choice = (
        ('No Offer','Currently No offer for this item'),
        ('10% Off','10 percent off for this item'),
        ('25% Off','25 percent off for this item'),
        ('Buy 1 Get 1','Buy one of this item and get other one free'),
    )
    offers = models.CharField(max_length=50, choices=offer_choice, default="No Offer")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

class Rice(Products):
    pass

class Bakery(Products):
    pass

class Dairy_products(Products):
    pass

class Drinks(Products):
    pass

class Spices(Products):
    pass

