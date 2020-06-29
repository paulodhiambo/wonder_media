from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    image = models.ImageField(null=True)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Users"
        verbose_name = "User"
