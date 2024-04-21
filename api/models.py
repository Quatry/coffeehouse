from django.db import models


class CoffeeHouse(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.CharField()
    date_created = models.DateTimeField(auto_now_add=True)
    info = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=50)
    coffeehouse = models.ForeignKey(CoffeeHouse, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    CHOICES = [
        ('ML', 'Мл'),
        ('L', 'Л'),
        ('GR', 'Гр'),
        ('KG', 'Кг'),
    ]
    name = models.CharField(max_length=50)
    measure_unit = models.CharField(choices=CHOICES)
    units = models.IntegerField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='menu_item_photo/', null=True)

    def __str__(self):
        return self.name
