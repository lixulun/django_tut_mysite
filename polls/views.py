from django.db.models import F
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class Index(generic.ListView):
    model = Question
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class Detail(generic.DetailView):
    pk_url_kwarg = "question_id"
    model = Question
    template_name = "polls/detail.html"
    context_object_name = "question"


class Results(generic.DetailView):
    pk_url_kwarg = "question_id"
    model = Question
    template_name = "polls/results.html"
    context_object_name = "question"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "你没有做出选择"},
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
