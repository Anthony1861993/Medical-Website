from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

#from django.template import loader

from .models import Question, Choice

#from django.http import Http404

'''
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	context = {
    	'latest_question_list': latest_question_list,
	}
	#return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)

	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)
'''

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]
'''
def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html', {'question': question})
'''
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


def results(request, question_id, hehe):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question, 'hehe': [15, 16], 'huhu': [15, 20]})

'''
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
'''

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		hehe = request.POST.getlist('hehe')
		
		print hehe
		
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		
		#hehe = (request.POST['hehe']? request.POST['hehe']: 0)

		# use this for getting a list of variables for a parameter
		#request.GET.getlist('myvar')

		return HttpResponseRedirect(reverse('polls:results', args=(question.id, 12, )))