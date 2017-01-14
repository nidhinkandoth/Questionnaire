from django.shortcuts import render
from questionnaire.models import Questionnaire
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests


def questionnaire(request):
	questions = Questionnaire.objects.all()
	context = {'questions':questions}
	return render(request, 'questionnaire.html', context)


@csrf_exempt	
def answers(request):
	questions = Questionnaire.objects.all()
	score = 0
	for question in questions:
		print question.question
		correct_answer = question.answer
		entered_answer = request.POST.get(question.question)
		if(entered_answer == correct_answer):
			score+=1
		print entered_answer
		print correct_answer
		
	print score
	context = {'score':score}
	return render(request, 'answer.html', context)
    
