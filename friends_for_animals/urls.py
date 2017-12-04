"""friends_for_animals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="home"),
    url(r'^events/$', views.events, name="events"),
    url(r'^medication/$', views.medication, name="medications"),
    url(r'^volunteers/$', views.volunteer, name="volunteers"),
    url(r'^about/$', views.about_us, name="about"),
    url(r'^contact/$', views.contact_us, name="contact"),
    url(r'^adoptions/$', views.adoptions, name="adoptions"),
    url(r'^donations/$', views.donations, name="donations"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
