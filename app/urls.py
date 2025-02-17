from django.urls import path
from app.views import (
    IndexPageAPIView, HomePageAPIView, LoginAPIView,
    TextAPIView, ImageAPIView, CodeAPIView, SettingsAPIView
)

urlpatterns = [
    path('api/index/', IndexPageAPIView.as_view(), name='index_api'),
    path('api/home/', HomePageAPIView.as_view(), name='home_api'),
    path('api/login/', LoginAPIView.as_view(), name='login_api'),
    path('api/text/', TextAPIView.as_view(), name='text_api'),
    path('api/image/', ImageAPIView.as_view(), name='image_api'),
    path('api/code/', CodeAPIView.as_view(), name='code_api'),
    path('api/settings/', SettingsAPIView.as_view(), name='settings_api'),
]
