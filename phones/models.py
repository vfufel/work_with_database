from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=15, decimal_places=1)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exists}, {self.slug}'
