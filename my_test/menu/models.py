from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, default='main_menu')


class MainMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='sub_menu')

    def __str__(self):
        return f'{self.name}'
