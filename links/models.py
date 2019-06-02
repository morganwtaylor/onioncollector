from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify

#extras
import numpy as np
import django_filters

class Category(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Link(models.Model):
    """
    Model used for Deep Web links
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING, related_name='links')
    created_at = models.DateTimeField(
            auto_now=True)
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length = 255)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING, related_name='links', null=True, blank=True)
    link = models.URLField(default = 'https://deepwebacademy.com')
    nsfw = models.BooleanField(default = False)
    votes = models.IntegerField(default = 1)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='link_likes')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        unique_together = ['user', 'title']

    def get_absolute_url(self):
        return reverse("links:detail", kwargs={'slug': self.slug})

    def average_rating(self):
        all_ratings = list(map(lambda x: x.rating, self.review_set.all()))
        return np.round(np.mean(all_ratings), decimals=2)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        super(Link, self).save(*args, **kwargs)

class Review(models.Model):
    """
    Allows users to review a links
    """
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Star'),
        (3, '3 Star'),
        (4, '4 Star'),
        (5, '5 Star')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    link = models.ForeignKey(Link, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    review = models.TextField(max_length=250, default="")
    rating = models.IntegerField(choices = RATING_CHOICES, default=1)

    def get_absolute_url(self):
        return reverse("links:all")


class LinkFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Link
        fields = ['title', 'description', 'link']
