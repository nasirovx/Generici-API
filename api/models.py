from django.db import models

class Contacts(models.Model):
    name = models.CharField(
        max_length=122,
        verbose_name='Полное имя',
        help_text='Введите полное имя контакта'
    )
    email = models.EmailField(
        max_length=122,
        verbose_name='Адрес электронной почты',
        help_text='Введите адрес эелектронной почты контакта'
    )
    phone = models.CharField(
        max_length=122,
        verbose_name='Номер телефона',
        help_text='Введите номер телефона'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введиет описание или дополнительную информацию'
    )
    
    def __str__(self):
        return self.name