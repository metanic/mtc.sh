import json

from django import http
from django import views

from django.views.decorators.cache import cache_page

from mtc.shorten import models

def location_from_identifier(identifier: str):
    try:
        return models.ShortenedLocation.objects.get_by_short_identifier(identifier)
    except ValueError as e:
        raise http.Http404(str(e))

@cache_page(60)
def preview(request: http.HttpRequest, *, identifier: bytes) -> http.HttpResponse:
    """ TODO: Make pretty someday? """

    return http.HttpResponse(json.dumps({
        'location': location_from_identifier(identifier).original_url,
    }))

@cache_page(3600)
def redirect(request: http.HttpRequest, *, identifier: bytes) -> http.HttpResponse:
    return http.HttpResponseRedirect(
        redirect_to=location_from_identifier(identifier).original_url,
    )