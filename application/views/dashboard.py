from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import render
from django.views import View


__all__ = (
    'IndexView',
    'Dashboard',
)


class IndexView(View):

    def get(self, request):
        return render(request, 'application/index.html')


@method_decorator(login_required, name='dispatch')
class Dashboard(View):

    def get(self, request):
        return render(request, 'application/dashboard.html')