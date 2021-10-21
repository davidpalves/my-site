from django.db import models

from common.models import IndexedTimeStampedModel


class ContactEmail(IndexedTimeStampedModel):
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return f"{self.email} - {self.created}"