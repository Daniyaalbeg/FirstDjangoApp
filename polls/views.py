from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question

#Full index function compared to shorter on at the bottom
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#Full detail function commented below
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = { 'question' : question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You are looking at results for question number %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)


#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)


#def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk = question_id)
#        context = {'question' : question}
#    except Question.DoesNotExsist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', context)
