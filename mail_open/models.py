from django.db import models


class MailOpen(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    mail = models.CharField('mail', max_length=100)

    class Meta:
        verbose_name = "MailOpen"
        verbose_name_plural = "MailOpen"
        ordering = ['-created']

    def __str__(self):
        return self.mail

    @staticmethod
    def count_unique_mails():
        return MailOpen.objects.order_by('mail').distinct('mail').count()
