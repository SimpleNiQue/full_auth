from django.shortcuts import render
from djoser.social.views import ProviderAuthView


class CustomProviderAuthView(ProviderAuthView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 201:
            pass

        return response
