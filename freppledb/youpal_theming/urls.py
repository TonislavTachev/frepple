from django.conf.urls import url
from . import views


autodiscover = True

urlpatterns = [
    url(r"^elements/$", views.ElementsDemo)
]