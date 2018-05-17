from django import urls

urlpatterns = [
    urls.path('', urls.include('mtc.shorten.urls')),
]
