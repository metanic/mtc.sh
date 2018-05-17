from django.db.models import Manager
from django.db.models.query import QuerySet

from mtc.shorten import util


class ShortenedLocationManager(Manager):
    def by_short_identifier(self, identifier: str) -> QuerySet:
        return self.filter(util.decode(identifier))

    def get_by_short_identifier(self, identifier: str) -> 'ShortenedLocation':
        return self.get(pk=util.decode(identifier))
