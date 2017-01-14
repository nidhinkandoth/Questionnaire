from django.shortcuts import render
from questionnaire.models import Questionnaire # Import the model classes
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests


def questionnaire(request):
	questions = Questionnaire.objects.all()
	context = {'questions':questions}
	return render(request, 'questionnaire.html', context)


	
def answers(request):
	questions = Questionnaire.objects.all() #fetches the query set.
	score = 0 #initially score is zero.
	for question in questions:
		correct_answer = question.answer #fetches answer given in the model.
		entered_answer = request.POST.get(str(question.id)) #fetches entered answer by the candidate
		if(entered_answer == correct_answer): #checks the entered answer is correct or not
			score+=1 #if correct score is incremented by one.

	context = {'score':score}
	return render(request, 'answer.html', context)
    
