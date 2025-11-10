from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cpu-test/", views.cpu_test, name="cpu_test"), #Only for testing purposes/csak a tesztelés miatt
]