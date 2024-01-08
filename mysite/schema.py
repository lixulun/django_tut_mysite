import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension

from polls.types import Question

@strawberry.type
class Query:
    questions: list[Question] = strawberry_django.field()
    
    
schema = strawberry.Schema(query=Query, extensions=[DjangoOptimizerExtension])