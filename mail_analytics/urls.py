from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mail_open.views import mail_open_request

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<mail>[0-9A-Za-z_\-@.]+)/pixel.png', mail_open_request),
]
