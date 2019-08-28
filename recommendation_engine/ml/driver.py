from os import path

from turicreate import load_model


class RecommendationEngine:

    def __init__(self, model_path):
        self._model = load_model(model_path)

    @classmethod
    def load(cls, model_path):
        if path.exists(model_path):
            return cls(model_path=model_path)
        raise FileNotFoundError("Model artifacts not found.")

    def json_serializer(self, sframe):
        data = {
            "top_recommendation": None,
            "score": None,
            "estimator": self._model._name(),
        }
        df = sframe.to_dataframe().set_index("StockCode")
        data["top_recommendation"] = df.index.tolist()
        data["score"] = df.score.to_dict()
        return data

    def for_user(self, user, k=10):
        result = self._model.recommend([user], k=k)
        return self.json_serializer(result)

    def from_interaction(self, items, k=10):
        result = self._model.recommend_from_interactions(
            observed_items=items,
            k=k,
        )
        return self.json_serializer(result)
