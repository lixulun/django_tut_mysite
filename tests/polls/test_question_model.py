import datetime
from django.utils import timezone
from polls.models import Question


def test_was_published_recently_with_future_question():
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    assert future_question.was_published_recently() == False


def test_was_published_recently_with_recent_question():
    time = timezone.now() - datetime.timedelta(hours=10)
    future_question = Question(pub_date=time)
    assert future_question.was_published_recently() == True


def test_was_published_recently_with_old_question():
    time = timezone.now() - datetime.timedelta(hours=25)
    future_question = Question(pub_date=time)
    assert future_question.was_published_recently() == False
