from .models import Quiz
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        field = ('title', 'body', 'answer')