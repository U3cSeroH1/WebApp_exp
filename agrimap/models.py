from django.db import models


class latlng(models.Model):
    # id = AutoField(primary_key=True)  # �����I�ɒǉ������̂Œ�`�s�v

    lat = models.lat(max_length=255, unique=True)
    lng = models.lng(max_length=255, unique=True)