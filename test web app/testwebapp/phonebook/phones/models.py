from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField("Имя", max_length=20)
    phone = models.CharField("Телефон", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
