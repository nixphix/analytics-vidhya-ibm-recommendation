from django.urls import path

from recommendation_engine import views

urlpatterns = [
    path("user", views.recommend_user, name="user-based"),
    path("items", views.recommend_from_interactions, name="item-based"),
]
