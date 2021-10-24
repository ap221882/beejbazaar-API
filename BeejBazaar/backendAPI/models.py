from django.db import models
from django.db.models.base import Model
from django.core import validators


# Create your models here.
class Product(models.Model):
    SEED = 'Seed'
    PLANT = 'Plant'
    PRODUCT_CHOICES = (
        (SEED, 'Seed'),
        (PLANT, 'Plant'),
    )
    name = models.CharField(choices=PRODUCT_CHOICES, max_length=32)

    def __str__(self):
        return self.name


class CategorySeed(models.Model):
    name = models.CharField(max_length=32, null=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(
        CategorySeed,
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return str(self.name)


class Seller(models.Model):
    name = models.CharField(max_length=64)
    contactNumber = models.IntegerField()
    seeds = models.ManyToManyField('SeedItem', through='Sold')

    def __str__(self):
        return str(self.name)


class SeedItem(models.Model):
    BAD = 1
    NOT_BAD = 2
    AVERAGE = 3
    NICE = 4
    EXCELLENT = 5

    MEMBER_CHOICES = (
        (BAD, 'Bad'),
        (NOT_BAD, 'Not Bad'),
        (AVERAGE, 'Average'),
        (NICE, 'Nice'),
        (EXCELLENT, 'Excellent'),
    )
    title = models.CharField(max_length=32, default='Seed')
    info = models.CharField(max_length=500)
    sellers = models.ManyToManyField('Seller',
                                     through='Sold',
                                     related_name='seller')
    price = models.IntegerField()
    Rating = models.IntegerField(
        choices=MEMBER_CHOICES,
        default=AVERAGE,
    )
    light = models.CharField(max_length=32, blank=True)
    watering = models.CharField(max_length=64, blank=True)
    time_till_harvest = models.CharField(max_length=32, blank=True)
    where_to_grow = models.CharField(max_length=32, blank=True)
    seasonal_information = models.CharField(max_length=32, blank=True)
    category = models.ForeignKey(CategorySeed,
                                 on_delete=models.CASCADE,
                                 default='',
                                 related_name='category')
    sub_category = models.ForeignKey(SubCategory,
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE,
                                     default='',
                                     related_name='sub_category')

    def __str__(self):
        return self.title


class Sold(models.Model):
    seller = models.ForeignKey(Seller,
                               on_delete=models.CASCADE,
                               related_name='sellers')
    seed_item = models.ForeignKey(SeedItem,
                                  on_delete=models.CASCADE,
                                  related_name='seeds')
