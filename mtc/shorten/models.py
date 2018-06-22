from mtc.core import models

from mtc.shorten import managers

class ShortenedLocation(models.CreateUpdateModel):
    identifier = models.TextField(primary_key=True)
    original_url = models.URLField()

    objects = managers.ShortenedLocationManager()