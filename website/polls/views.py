from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question,Choice
from django.shortcuts import render_to_response
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

def index(request):
    latest_poll_list = Question.objects.order_by('-pub_date')[:5]
    return render_to_response('yoyo/index.html', locals())
    #return HttpResponse("Hello, world. You're at the polls index.")
    
def detail(request, poll_id):
   # try:
   #     poll = Question.objects.get(pk=poll_id)
   # except Exception, e:#Poll.DoesNotExist:
   #     raise Http404
    poll = get_object_or_404(Question, pk=poll_id)
    #return render_to_response('yoyo/detail.html', locals())
    return render(request, 'yoyo/detail.html', {'poll': poll})
    #return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    poll = get_object_or_404(Question, pk=poll_id)
    return render(request, 'yoyo/results.html', {'poll': poll})
    #return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Question, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'yoyo/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    #return HttpResponse("You're voting on poll %s." % poll_id)    
    

def hehe(request):
    return render(request, "yoyo/index.html")