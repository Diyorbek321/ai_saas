from django import urls
from django.urls import path
from app.views import IndexPageTemplateView,HomePageTemplateView,LoginPage,TextPage
urlpatterns = [
    path('index/',IndexPageTemplateView.as_view(),name='index'),
    path('home/',HomePageTemplateView.as_view(),name='home'),
    path('login/',LoginPage.as_view(),name='login'),
    path('text/',TextPage.as_view(),name='text')
]