from django.conf.urls import patterns, include, url

from observer.views import HomePageView

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(template_name="observer/index.html"), name='index'),
)
