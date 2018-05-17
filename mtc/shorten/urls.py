from django import urls

from mtc.shorten import views

urlpatterns = (
  urls.path('preview/<str:identifier>', views.preview),
  urls.path('<str:identifier>', views.redirect),
)