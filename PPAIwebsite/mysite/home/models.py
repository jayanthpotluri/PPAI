from django.db import models

from wagtail.models import Page


from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class Values(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    membership = models.CharField(max_length=100)
    class Meta:
        db_table="user"
