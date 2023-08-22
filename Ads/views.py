from rest_framework.decorators import api_view
from rest_framework.response import Response
from Ads.automoto import scrape_single_ad
from Ads.mobile import scrape_single_ad_mobile
from .models import Ads, Image, MainImage, Price
from .serializers import AdsSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from Ads.serializers import UserSerializer
from django.core.management import call_command

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

@api_view(['GET', 'POST'])
def add_url(request):
    if request.method == 'GET':
        ads = Ads.objects.all()
        serializer = AdsSerializer(ads, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        url = data.get("data")
        ad_data = None
        
        if "automoto.bg" in url:
            ad_data = scrape_single_ad(url)
        elif "mobile.bg" in url:
            ad_data = scrape_single_ad_mobile(url)
        else:
            print("Грешен URL")

        if ad_data:
            image_urls = ad_data.pop("image_urls")
            price = ad_data.pop("price")

            try:
                ad_instance = Ads.objects.get(url=url)
                Price.objects.create(price=price, ad=ad_instance)  # Create a new Price instance with the scraped price
                return Response({"message": "Ad already exists"})
            except Ads.DoesNotExist:
                ad_instance = Ads.objects.create(**ad_data)

                image_instances = []
                for image_url in image_urls:
                    image_instance, created = Image.objects.get_or_create(ad=ad_instance, image=image_url)
                    image_instances.append(image_instance)
                
                ad_instance.images.set(image_instances)
                price_instance = Price.objects.create(price=price, ad=ad_instance)
                
                print('Success: Data processed and saved')
        else:
            print('Error: Failed to scrape ad information')
        
        return Response({"message": "Raboti"})
