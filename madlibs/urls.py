from django.urls import path
from . import views

urlpatterns = [
    path("madlibsform/", views.madlibs_view, name="madlibsform")
]
