import string
from random import random

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from app.forms import RegisterForm
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import UserAction, GeneratedCode  # We’ll define this next

# Index page (public landing page)
class IndexPageTemplateView(TemplateView):
    template_name = 'index.html'

# Dashboard (protected, shows user actions)
@method_decorator(login_required, name='dispatch')
class HomePageTemplateView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch only the current user's actions
        context['actions'] = UserAction.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        action_text = request.POST.get('action')
        if action_text:
            UserAction.objects.create(user=request.user, action=action_text)
            messages.success(request, 'Action added successfully!')
        return redirect('home')

# Registration view (already good, just tweaking)
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

# Login view (new)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# Logout view (new)
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')  # Back to public index page

# Other pages (protected with login_required where it makes sense)
@method_decorator(login_required, name='dispatch')
class TextPage(TemplateView):
    template_name = 'text.html'

@method_decorator(login_required, name='dispatch')
class Image(TemplateView):
    template_name = 'image.html'


@method_decorator(login_required, name='dispatch')
class Code(TemplateView):
    template_name = 'code.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch user's saved codes
        context['codes'] = GeneratedCode.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # AJAX request
            data = json.loads(request.body)
            code = data.get('code')
            language = data.get('language')
            title = data.get('title', f"Generated {language} Code")

            if code and language:
                # Save the generated code
                GeneratedCode.objects.create(
                    user=request.user,
                    code=code,
                    title=title,
                    # You could add a language field to the model if needed
                )
                return JsonResponse({'success': True, 'message': 'Code saved successfully!'})
            return JsonResponse({'success': False, 'message': 'Invalid code or language'}, status=400)

        # Fallback for non-AJAX POST (if needed)
        return redirect('code')
@method_decorator(login_required, name='dispatch')
class Settings(TemplateView):
    template_name = 'setting.html'

@method_decorator(login_required, name='dispatch')
class Project(TemplateView):
    template_name = 'project.html'

@method_decorator(login_required, name='dispatch')
class Template(TemplateView):
    template_name = 'template.html'

@method_decorator(login_required, name='dispatch')
class Support(TemplateView):
    template_name = 'support.html'

@method_decorator(login_required, name='dispatch')
class Data(TemplateView):
    template_name = 'data.html'

@method_decorator(login_required, name='dispatch')
class Resources(TemplateView):
    template_name = 'resources.html'

@method_decorator(login_required, name='dispatch')
class ProjectDetail(TemplateView):
    template_name = 'project_detail.html'

@method_decorator(login_required, name='dispatch')
class REsourcesDetail(TemplateView):
    template_name = 'resorces-detail.html'  # Note: typo? Should it be 'resources-detail.html'?