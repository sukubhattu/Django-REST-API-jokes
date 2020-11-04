from django.urls import path
from .views import JokesList, JokeDetail, JokeRandom

urlpatterns = [
    path("", JokesList.as_view(), name="jokes_list"),
    path("<int:pk>/", JokeDetail.as_view(), name="joke_detail"),
    path("random/", JokeRandom.as_view(), name="random_joke")
]
