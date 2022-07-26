"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from first import views

router = DefaultRouter()
router.register("", views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('dj-rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login'),
     path('dj-rest-auth/twitter/', views.TwitterLogin.as_view(), name='twitter_login'),
    path('dj-rest-auth/google/', views.GoogleLogin.as_view(), name='google_login'),
  
 
   
]

    # path('', TemplateView.as_view(
    #     template_name='doc.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='api_doc'),

    

urlpatterns += router.urls