from django.db import models

# Create your models here.
class item(models.Model):

    #Fields
    inventory_no = models.CharField(max_length=8)
    loc = models.CharField(max_length = 5)
    owner = models.CharField(max_length = 20)
    desc = models.TextField()
    brand = models.CharField(max_length = 20,  blank=True)
    price = models.IntegerField()
    purchase_date = models.DateTimeField()

    #Methods
    def __str__(self):
        return 'item #{}'.format(self.inventory_no)
    
    class Meta:
        verbose_name_plural = 'items'