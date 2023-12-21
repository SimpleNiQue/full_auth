from .views import CustomProviderAuthView
from django.urls import path, re_path
urlpatterns = [
    re_path(r'^o/(?P<provider>\S+)/$', 
         CustomProviderAuthView.as_view(), 
         name='provider-auth')
]