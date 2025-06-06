from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Booking(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    guest_num = models.IntegerField(_("Guest number"))
    booking_date = models.DateField(_("Booking date"))
    
    class Meta:
        verbose_name = 'Booking'
        ordering = ['-id']
    
    def __str__(self):
        return str(self.id) 
    
class Menu(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    inventory = models.IntegerField(_("Inventory"))

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
        ordering = ['-id']
    
    def __str__(self):
        return f'{self.title} : {self.price}' 