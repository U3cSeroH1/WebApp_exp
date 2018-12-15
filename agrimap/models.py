from django.db import models

class latlng(models.Model):
    # id = AutoField(primary_key=True)

    lat = models.CharField(unique=True)
    lng = models.CharField(unique=True)



    def __str__(self):
        return self.lat
