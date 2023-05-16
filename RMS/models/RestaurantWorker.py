from django.db import models
from .RestaurantAvailability import RestaurantAvailability
from .RestaurantWorkerRole import RestaurantWorkerRole
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator


class RestaurantWorker(models.Model):

    class Meta:
            abstract = True

        name = models.CharField(max_length=200,
                                validators=[MinLengthValidator(limit_value=2,
                                                               message='Name must be at least 2 characters long.')])
#----------------------------------------------------------------------------------------------------------------
    role = models.ForeignKey(RestaurantWorkerRole, on_delete=models.CASCADE)
    availability = models.ForeignKey(RestaurantAvailability, on_delete=models.CASCADE)
#----------------------------------------------------------------------------------------------------------------
