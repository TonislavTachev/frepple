from django.conf.urls import url
from . import views


autodiscover = True

urlpatterns = [
    url(r"^elements/$", views.ElementsDemo),
    url(r"^elements/base$", views.BaseSite),
     url(r"^grid$", views.BaseMain)
]