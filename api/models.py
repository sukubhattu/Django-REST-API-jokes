from django.db import models


class Jokes(models.Model):
    punchLine = models.TextField(max_length=500)
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "jokes"

    def __str__(self):
        # returning first 50 character
        return (self.punchLine[0:50] + "...")
