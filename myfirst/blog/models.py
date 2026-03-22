from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def short_description(self):
        return ' '.join(self.description.split()[:30])

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)  # nowa kolumna cena
    stock = models.PositiveIntegerField(default=0)               # stan magazynowy
    category = models.CharField(max_length=100, blank=True)      # kategoria
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def short_description(self):
        return ' '.join(self.description.split()[:30])

    def __str__(self):
        return self.name
