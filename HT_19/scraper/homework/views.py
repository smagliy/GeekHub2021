from django.shortcuts import render
from .tasks import new, ask, show, job


def index(request):
    value = request.POST.get('news_category')
    if value == 'new':
        new.delay()
    elif value == 'ask':
        ask.delay()
    elif value == 'show':
        show.delay()
    elif value == 'job':
        job.delay()
    return render(request, 'homework/index.html')
