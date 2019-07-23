from django.db import models


class MyDetailModel(models.Model):
    name = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name


class MyModel(models.Model):
    name = models.CharField(max_length=10, default="")
    detail = models.OneToOneField(MyDetailModel, default="")

    def __str__(self):
        return self.name
