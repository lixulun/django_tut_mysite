import strawberry_django
from strawberry import auto

from . import models

@strawberry_django.type(models.Question)
class Question:
    id: auto
    question_text: str
    pub_date: auto
    choice_set: list['QuestionChoice']
    
    
@strawberry_django.type(models.Choice)
class QuestionChoice:
    id: auto
    choice_text: str
    votes: int
    question: Question