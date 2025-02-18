from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import login
from django.urls import reverse_lazy
from app.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
class IndexPageTemplateView(TemplateView):
    template_name = 'index.html'
@method_decorator(login_required, name='dispatch')
class HomePageTemplateView(TemplateView):
    template_name = 'dashboard.html'


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Auto-login after registration
            return redirect(reverse_lazy('home'))  # Redirect to dashboard
        return render(request, 'login.html', {'form': form})
class TextPage(TemplateView):
    template_name = 'text.html'

class Image(TemplateView):
    template_name = 'image.html'

class Code(TemplateView):
    template_name = 'code.html'

class Settings(TemplateView):
    template_name = 'setting.html'

class Project(TemplateView):
    template_name = 'project.html'

class Template(TemplateView):
    template_name = 'template.html'

class Support(TemplateView):
    template_name = 'support.html'

class Data(TemplateView):
    template_name = 'data.html'

class Resources(TemplateView):
    template_name = 'resources.html'