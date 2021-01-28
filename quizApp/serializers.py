from .models import Quiz
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerilaizer):
    class Meta:
        model = Quiz
        field = ('title', 'body', 'answer')