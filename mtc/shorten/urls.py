from django import urls

from mtc.shorten import views

urlpatterns = (
  urls.path('_/<str:identifier>', views.preview),
  urls.path('<str:identifier>', views.redirect),
)
