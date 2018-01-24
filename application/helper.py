import uuid

from django.conf import settings


def upload_file(instance, filename):
    file_name = str(uuid.uuid4()) + "." + filename.split(".")[-1]

    if instance.type and instance.type_model:
        return "%s/%s/%s" % (instance.type_model, instance.type, file_name)
    elif instance.type or instance.type_model:
        return "%s/%s" % (instance.type if instance.type else instance.type_model, file_name)

    return file_name


def get_storage_path():
    """
    Path to s3 media
    """
    return settings.MEDIA_LOCATION


def get_server_storage_path():
    """
    Path to server side media
    """
    return '/'.join([settings.BASE_DIR, 'media'])
