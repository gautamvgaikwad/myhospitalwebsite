from django.db import models


class Hosp(models.Model):
    col1 = models.CharField(max_length=20)
    col2 = models.CharField(max_length=20)
