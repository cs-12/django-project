from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.urls import reverse
from .models import Question,Choice
from django.http import HttpResponseRedirect


def index(request):
    latest_question_list=Question.objects.all()
    context={'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{ 'question': question})


def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{ 'question': question})


def vote(request, question_id):
    # print(request.POST['choice'])
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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.reverse
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
            
