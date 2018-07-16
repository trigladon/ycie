from django.middleware.locale import LocaleMiddleware as DjLocaleMiddleware
from django.utils import translation
from django.conf import settings


class LocaleMiddleware(DjLocaleMiddleware):

    def process_response(self, request, response):
        response = super(LocaleMiddleware, self).process_response(request, response)
        if response.status_code != 404:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, translation.get_language())
        return response