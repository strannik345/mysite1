from django.db import models


class temperature(models.Model):
	date = models.DateTimeField(primary_key=True)
	temperature = models.FloatField()

