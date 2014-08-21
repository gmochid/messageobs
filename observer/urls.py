from django.conf.urls import patterns, include, url

from observer.views import HomePageView, HomeLoginView

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(template_name="observer/index.html"), name='index'),
    url(r'^login$', HomeLoginView.as_view(template_name="observer/index.html"), name='index'),
)
