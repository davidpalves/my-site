# -*- coding: utf-8 -*-
from django import utils
from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.utils.text import slugify

from markdown import markdown
from readtime import of_markdown

from blog.choices import POST_STATUS_CHOICES
from users.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    slug = models.SlugField(max_length=150, unique=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(
        choices=POST_STATUS_CHOICES,
        default=POST_STATUS_CHOICES.draft,
        blank=False,
        null=False,
        max_length=10,
    )
    text = models.TextField()
    tags = models.CharField(max_length=255, blank=True)

    created_date = models.DateField(auto_now_add=True)
    published_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.tags = ", ".join(
            {tag.strip() for tag in self.tags.split(",")}
        )
        super(Post, self).save(*args, **kwargs)

    def get_text_as_markdown(self):
        return mark_safe(markdown(self.text, safe_mode="escape"))

    @property
    def read_time(self):
        return of_markdown(self.text, wpm=225).minutes
    
    def publish(self):
        if self.status is not PostStatusEnum.published:
            self.published_date = timezone.now()
            self.status = POST_STATUS_CHOICES.published
            self.save()

    def archive(self):
        if self.status is not POST_STATUS_CHOICES.archived:
            self.status = POST_STATUS_CHOICES.archived
            self.save()

    def draft(self):
        if self.status is not POST_STATUS_CHOICES.draft:
            self.status = POST_STATUS_CHOICES.draft
            self.save()

    def __str__(self):
        return self.title
