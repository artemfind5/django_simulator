"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from untitled import views
from django.views.generic.base import TemplateView
from untitled.views import IndexView
from untitled.n13.views import main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('13', main, name='13'),
    path('42', main, name='42'),
    path('70', main, name='70'),
    path('', IndexView.as_view(template_name="index.html"), name="home"),
    path('fun', IndexView.as_view(template_name="fun.html"), name="fun"),
    path('temp', IndexView.as_view(template_name="temp.html"), name="temp"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)