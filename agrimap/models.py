from django.db import models


class latlng(models.Model):
    # id = AutoField(primary_key=True)

    lat = models.lat(max_length=255, unique=True)
    lng = models.lng(max_length=255, unique=True)



    def __str__(self):
        return self.lat, self.lng
