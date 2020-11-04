from django.urls import path
from .views import JokesList, JokeDetail, JokeRandom

urlpatterns = [
    path("", JokesList.as_view()),
    path("<int:pk>/", JokeDetail.as_view()),
    path("random/", JokeRandom.as_view())
]
