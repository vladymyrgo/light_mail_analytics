from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import get_storage_class
from django.core.files.images import ImageFile

from mail_open.models import MailOpen


def mail_open_request(request, mail):
    MailOpen.objects.create(mail=mail)

    storage_class = get_storage_class(settings.STATICFILES_STORAGE)
    storage = storage_class()
    image = ImageFile(storage.open("images/FFFFFF-1.png"))
    image.storage = storage

    return HttpResponse(image, content_type="image/png")
