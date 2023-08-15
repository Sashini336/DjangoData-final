from rest_framework import serializers
from .models import Ads, MainImage, Image, Price
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class MainImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainImage
        fields = ['image']
        
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']
        

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Price
        fields = ['price', 'date']
        
        
class AdsSerializer(serializers.ModelSerializer):
    main_image = MainImageSerializer()
    images = ImageSerializer(many=True)
    price = PriceSerializer(many=True)
    class Meta: 
        model = Ads
        fields = ['id', 'url', 'title', 'price', 'year', 'millage', 'fuel_type', 'transmission', 'horsepower', 'color', 'more_information', 'main_image', 'images']
