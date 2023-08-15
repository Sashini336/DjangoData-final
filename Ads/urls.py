from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdsViewSet, add_url
from .models import Ad
from serializers import AdsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.urlpatterns import format_suffix_patterns
from Ads import views

router = DefaultRouter()
router.register(r'ads', AdsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ads', views.ads_list),
    path('ads/<int:id>/', views.ads_detail),
    path('add_url/', add_url, name='add-url'),  
]

urlpatterns = format_suffix_patterns(urlpatterns)
