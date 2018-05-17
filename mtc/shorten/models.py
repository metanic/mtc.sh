from mtc.core import models

from mtc.shorten import managers

class ShortenedLocation(models.CreateUpdateModel):
    original_url = models.URLField()
    objects = managers.ShortenedLocationManager()