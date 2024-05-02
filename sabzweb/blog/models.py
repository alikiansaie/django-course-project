from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


# Managers


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


# Create your models here.


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'
        REJECTED = 'RJ', 'Rejected'

    # relation
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_posts',
        verbose_name='نویسنده'
    )
    # data field
    title = models.CharField(
        max_length=250,
        verbose_name='عنوان'
    )

    description = models.TextField(
        verbose_name='توضیحات'
    )

    slug = models.SlugField(
        max_length=250,
        verbose_name='اسلاگ'
    )

    # Date
    publish = jmodels.jDateTimeField(
        default=timezone.now,
        verbose_name='تاریخ انتشار'
    )

    created = jmodels.jDateTimeField(
        auto_now_add=True,
    )

    updated = jmodels.jDateTimeField(
        auto_now=True,
    )

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='وضعیت'
    )

    objects = models.Manager()
    published = PublishManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title
