import json

from django import http
from django import views

from mtc.shorten import models

def location_from_identifier(identifier: str):
    return models.ShortenedLocation.objects.get_by_short_identifier(identifier)

def preview(request: http.HttpRequest, *, identifier: bytes) -> http.HttpResponse:
    """ TODO: Make pretty someday? """

    return http.HttpResponse(json.dumps({
        'location': location_from_identifier(identifier).original_url,
    }))


def redirect(request: http.HttpRequest, *, identifier: bytes) -> http.HttpResponse:
    return http.HttpResponseRedirect(
        redirect_to=location_from_identifier(identifier).original_url,
    )