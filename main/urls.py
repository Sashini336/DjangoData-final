from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Ads.views import AdsViewSet, UserViewSet, add_url

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ads', AdsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('add_url/', add_url, name='add_url'),  
    path('', include(router.urls)),
]
