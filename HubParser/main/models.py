from django.db import models


class Hub(models.Model):
    url = models.URLField(unique=True)
    period = models.IntegerField(default=600)

    def __str__(self):
        return self.url