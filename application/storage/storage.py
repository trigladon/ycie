from django.core.files.storage import FileSystemStorage
from django.conf import settings

from storages.backends.s3boto import S3BotoStorage

from application.storage.helper import get_storage_path, get_server_storage_path


__all__ = (
    'StaticStorage',
    'FileStorage',
    'get_file_storage',
)


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION


class FileStorage(S3BotoStorage):
    location = settings.MEDIA_LOCATION


def get_file_storage(*args, **kwargs):
    if settings.DEBUG:
        return FileSystemStorage(location=get_server_storage_path())
    return FileStorage(location=get_storage_path())
