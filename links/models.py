from django.db import models

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, related_name='links', null=True)
    created_at = models.DateTimeField(
            auto_now=True)
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length = 255)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, related_name='links', null=True, blank=True)
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
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

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
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    link = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=50, default='no review comment')
    # rating = models.CharField(max_length=1, choices=RATING_CHOICES)

    def get_absolute_url(self):
        return reverse("links:all")
