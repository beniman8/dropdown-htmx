from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=128)


class Module(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey(
        Course, related_name="modules", on_delete=models.CASCADE
    )
