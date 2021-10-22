# -*- coding: utf-8 -*-
from django import utils
from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.utils.text import slugify

from markdown import markdown

from blog.enums import PostStatusEnum, POST_STATUS_ENUM
from users.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    title = models.CharField(max_length=255, null=False, blank=False)

    slug = models.SlugField(max_length=150, unique=True)

    status = models.CharField(
        choices=POST_STATUS_ENUM, default=PostStatusEnum.DRAFT, blank=False, null=False, max_length=10
    )

    text = models.TextField()

    created_date = models.DateField(default=timezone.now)

    published_date = models.DateField(blank=True, null=True)

    tags = models.ManyToManyField('Tag', related_name="posts", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_text_as_markdown(self):
        return mark_safe(markdown(self.text, safe_mode="escape"))

    def publish(self):
        if self.status is not PostStatusEnum.PUBLISHED:
            self.published_date = timezone.now()
            self.status = PostStatusEnum.PUBLISHED
            self.save()

    def archive(self):
        if self.status is not PostStatusEnum.ARCHIVED:
            self.status = PostStatusEnum.ARCHIVED
            self.save()

    def draft(self):
        if self.status is not PostStatusEnum.DRAFT:
            self.status = PostStatusEnum.DRAFT
            self.save()

    def __str__(self):
        return self.title


class Tag(models.Model):
    label = models.CharField(max_length=50)
    