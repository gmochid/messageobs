from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from observer.models import Surat

class HomePageView(ListView):
    model = Surat
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['is_logged_in'] = self.request.user.is_authenticated()
        return context

class HomeLoginView(TemplateView):
    template_name = "observer/login.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomeLoginView, self).get_context_data(**kwargs)
        return context
