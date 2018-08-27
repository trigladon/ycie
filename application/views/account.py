from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import render
from django.views import View


__all__ = (
    'Account',
)


@method_decorator(login_required, name='dispatch')
class Account(View):

    def get(self, request):
        return render(request, 'application/account/index.html')
