from django.urls import path, include
from .views import randomQuizAPI

urlpatterns = [
    path('<int:id>/',randomQuizAPI),
]