from django.conf.urls import url, include
from django.conf import settings
from blogs.views import DaywiseArchiveView, ArticleListView, ArticleDetailView
# from django.urls import path
from django.views.generic.dates import ArchiveIndexView, DateDetailView
from blogs.models import Article



urlpatterns = [
	url(r'^archives/$', ArticleListView.as_view(), name="article-list"),
	# Example: /2012/nov/10/
    url(r'^archives/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name="article-detail"),
]