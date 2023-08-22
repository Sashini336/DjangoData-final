from django.db import models


class MainImage(models.Model):
    image = models.CharField(max_length=255, default='')


class Ads(models.Model):
    url = models.CharField(max_length=255, default='', blank=True)
    title = models.CharField(max_length=255, default='', blank=True, null=True)
    year = models.CharField(max_length=255, default='', blank=True , null=True)
    millage = models.CharField(max_length=255, default='', blank=True, null=True)
    fuel_type = models.CharField(max_length=255, default='',blank=True, null=True)
    transmission = models.CharField(max_length=255, default='', blank=True, null=True)
    horsepower = models.CharField(max_length=255, default='', blank=True, null=True)
    color = models.CharField(max_length=255, default='', blank=True , null=True)
    more_information = models.CharField(max_length=3000, default='' , blank=True, null=True)
    main_image = models.CharField(default='', max_length=255)
    
    def __str__(self):
        return self.title
    


class Image(models.Model):
    image = models.CharField(max_length=255, default='')
    ad = models.ForeignKey(Ads,default='', related_name='images', max_length=255, on_delete=models.CASCADE)
    
    
class Price(models.Model):
    price = models.CharField(max_length=255, default='')
    date = models.DateField((""),auto_now_add=True)
    ad = models.ForeignKey(Ads, default='', related_name='price', max_length=255, on_delete=models.CASCADE)
    class Meta:
        ordering = ['date']