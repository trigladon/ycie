from django.conf import settings as djsettings


def settings(request):
    return {
        'SITE_NAME': djsettings.SITE_NAME
    }