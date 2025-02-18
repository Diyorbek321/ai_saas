from django import urls
from django.urls import path
from app.views import IndexPageTemplateView,HomePageTemplateView,LoginPage,TextPage,Image,Code,Settings,Project,Template
urlpatterns = [
    path('index/',IndexPageTemplateView.as_view(),name='index'),
    path('home/',HomePageTemplateView.as_view(),name='home'),
    path('login/',LoginPage.as_view(),name='login'),
    path('text/',TextPage.as_view(),name='text'),
    path('image/',Image.as_view(),name='image'),
    path('code/',Code.as_view(),name='code'),
    path('setting/',Settings.as_view(),name='setting'),
    path('project/',Project.as_view(),name='project'),
    path('template/',Template.as_view(),name='template')
]