from django.shortcuts import render
from django.views import View


__all__ = (
    'About',
    'Contact'
)


class About(View):

    def get(self, request):
        return render(request, 'application/about.html')


class Contact(View):

    def get(self, request):
        return render(request, 'application/contacts.html')