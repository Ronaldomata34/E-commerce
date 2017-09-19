from django.db import models
from django.core.urlresolvers import reverse

from cloudinary.models import CloudinaryField


PLATFORM = (
    ('ps3', 'ps3'),
    ('ps4', 'ps4'),
)

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=200, db_index=True, choices=PLATFORM)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'platform'
        verbose_name_plural = 'platforms'

    def __str__(self):
        return self.name


class TypeOfGame(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'type of game'
        verbose_name_plural = 'types of games'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category_of_product')
    platform = models.ForeignKey(Platform, related_name='platform_of_product')
    typeofgame = models.ForeignKey(TypeOfGame, related_name='type_of_game')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = CloudinaryField('image')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', args=[self.id, self.slug])