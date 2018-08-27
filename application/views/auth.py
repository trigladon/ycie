from django.contrib.auth.views import (
    LoginView as DjLoginView,
    LogoutView as DjLogoutView
)
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View

from ..forms import AuthenticationForm

__all__ = (
    'SignIn',
    'SignUp',
    'SignOut',
)


class SignIn(DjLoginView):
    template_name = 'application/sign-in.html'
    form_class = AuthenticationForm


class SignUp(View):

    def get(self, request):
        return render(request, 'application/sign-up.html')

    def post(self, request):
        return JsonResponse({})


class SignOut(DjLogoutView):
    next_page = reverse_lazy('index')