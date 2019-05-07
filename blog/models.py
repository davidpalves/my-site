from django.utils.safestring import mark_safe
from django.db import models
from users.models import User
from django.utils import timezone
from markdown import markdown
from django.utils.text import slugify


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False)

    title = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    slug = models.SlugField(
        max_length=150,
        unique=True
        )

    text = models.TextField()

    created_date = models.DateTimeField(
        default=timezone.now
    )

    published_date = models.DateTimeField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_text_as_markdown(self):
        return mark_safe(markdown(self.text, safe_mode='escape'))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
