from django.contrib import admin
from mail_open.models import MailOpen


class MailOpenAdmin(admin.ModelAdmin):
    list_display = ['mail', 'created']
    fields = ['created', 'mail']
    readonly_fields = ['created']


admin.site.register(MailOpen, MailOpenAdmin)
