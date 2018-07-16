from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from . import decorators


class IndexView(View):

    def get(self, request):
        return render(request, 'application/index.html')


class SignIn(View):

    def get(self, request):
        return render(request, 'application/sign-in.html')

    @decorators.ajax
    def post(self, request):
        return JsonResponse({})


class SignUp(View):

    def get(self, request):
        return render(request, 'application/sign-up.html')

    @decorators.ajax
    def post(self, request):
        return JsonResponse({})


@method_decorator(login_required, name='dispatch')
class SignOut(View):

    def get(self, request):
        return render(request, 'application/sign-out.html')


@method_decorator(login_required, name='dispatch')
class Dashboard(View):

    def get(self, request):
        return render(request, 'application/dashboard.html')


@method_decorator(login_required, name='dispatch')
class Account(View):

    def get(self, request):
        return render(request, 'application/account/index.html')


class About(View):

    def get(self, request):
        return render(request, 'application/about.html')


class Contact(View):

    def get(self, request):
        return render(request, 'application/contacts.html')
