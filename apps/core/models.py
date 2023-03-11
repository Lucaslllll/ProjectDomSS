from django.db import models
# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=1024)
    preview = models.TextField()
    details = models.TextField()
    price = models.DecimalField(max_digits=16, decimal_places=2)
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

