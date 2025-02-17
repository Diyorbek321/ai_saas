from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexPageTemplateView(TemplateView):
    template_name = 'index.html'

class HomePageTemplateView(TemplateView):
    template_name = 'dashboard.html'

class LoginPage(TemplateView):
    template_name = 'login.html'

class TextPage(TemplateView):
    template_name = 'text.html'