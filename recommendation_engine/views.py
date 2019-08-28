import json

from django.conf import settings
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from recommendation_engine.ml import RecommendationEngine

ml_model = getattr(settings, "ML_MODEL_PATH")
recommend = RecommendationEngine.load(ml_model)


@api_view(['POST'])
def recommend_user(request):
    data = json.loads(request.body)
    user_id = data.get("user")
    k = data.get("k", 10)
    if user_id:
        prediction = recommend.for_user(user_id, k)
        return Response(prediction)
    raise Http404("user id is required.")


@api_view(['POST'])
def recommend_from_interactions(request):
    data = json.loads(request.body)
    items = data.get("items")
    k = data.get("k", 10)
    if items:
        prediction = recommend.from_interaction(items, k)
        return Response(prediction)
    raise Http404("items is required.")
