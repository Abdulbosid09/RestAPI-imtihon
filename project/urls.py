"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import DarsViewSet, KursViewSet, IzohViewSet, UserRegisterView, LikeBosishQismi , Email,LikeBosish
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register(r'dars', DarsViewSet)
router.register(r'kurs', KursViewSet)
router.register(r'izoh', IzohViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('dars/<int:pk>/like/', LikeBosishQismi.as_view()),
    path('dars/like/create/',LikeBosish.as_view()),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('api/v1/email/', Email.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
