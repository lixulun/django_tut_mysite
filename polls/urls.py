from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("<int:question_id>/", views.Detail.as_view(), name="detail"),
    path("<int:question_id>/results/", views.Results.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
