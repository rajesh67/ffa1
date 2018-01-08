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
    url(r'^chandu/raju/admin/', admin.site.urls),
    url(r'^$', views.index, name="home"),
    url(r'^programs/$', views.events, name="events"),
    url(r'^medication/$', views.MedicationView.as_view(), name="medications"),
    #url(r'^volunteers/$', views.volunteer, name="volunteers"),
    url(r'^volunteers/$', views.VolunteerCreateView.as_view(), name="volunteers"),
    #url(r'^volunteers/$', views.VolunteerView.as_view(), name="volunteers"),
    url(r'^thank-you/$', views.thank_you, name="thank-you"),
    url(r'^about/$', views.about_us, name="about"),
    url(r'^contact/$', views.contact_us, name="contact"),
    url(r'^adoptions/$', views.AdoptionView.as_view(), name="adoptions"),
    url(r'^thank-you/$', views.thank_you, name="thank-you"),
    # 
    url(r'^adoptions/new/$', views.AdoptionCreateView.as_view(), name="new-adoption-question"),
    url(r'^adoptions/update/(?P<pk>\d+)/$', views.AdoptionCreateView.as_view(), name="update-adoption-question"),
    # 

    url(r'^donations/$', views.DonationView.as_view(), name="donations"),
    url(r'^donors/$', views.DonorListView.as_view(), name="donors_list"),

    url(r'^blogs/', include('blogs.urls'), name="blogs"),

    url(r'^summernote/', include('django_summernote.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
