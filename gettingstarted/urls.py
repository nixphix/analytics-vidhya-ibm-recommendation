from django.urls import path, include
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path("recommend/", include("recommendation_engine.urls")),
]
