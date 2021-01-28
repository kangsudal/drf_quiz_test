from rest_framework.response import response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerilaizer
import random

@api_view(['GET'])
def randomQuizAPI(request, id):
    '''개수(id)가 주어졌을때 그 개수만큼 랜덤한 퀴즈 객체 반환해주는 API'''
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs),id)
    serializer = QuizSerilaizer(randomQuizs, many=True)
    return Response(serializer.data)