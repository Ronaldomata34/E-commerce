from django.db import models


class Product(models.Model):

    CATEGORY = {
        ('terror', 'terror' ),
        ('disparo', 'disparo'),
        ('deporte', 'deporte'),
        ('carrera', 'carrera'),
    }

    TYPEGAMES = {
        ('DLC', 'DLC'),
        ('Full Game', 'Full Game'),
        ('Season Pass', 'Season Pass')
    }

    CONSOLE = {
        ('Ps3', 'Ps3'),
        ('Ps4', 'Ps4'),
    }

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    category = models.CharField(max_length=255, choices=CATEGORY)
    console = models.CharField(max_length=255, choices=CONSOLE)
    description = models.TextField(blank=True)
    type_game = models.CharField(max_length=100, choices=TYPEGAMES)
    hard_disk_space = models.IntegerField()
    language = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    offer = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True, upload_to='media')

    def __str__(self):
        return self.name
