from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator


class ContactData(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20,
                             validators=[RegexValidator(regex='^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]'
                                                              '{4,6}$',
                                                        message='Enter valid phone number.')])
    email = models.EmailField()
    chatId = models.CharField(max_length=40,
                              validators=[MinLengthValidator(limit_value=6,
                                                             message='ID should be at least 6 characters long.')])

