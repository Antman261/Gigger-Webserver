from django.shortcuts import render
from main.models import Performer

# Create your views here.
def bookPerformer(request):
    context = {
        "performer": Performer.objects.get(pk=request.GET['p'])
    }
    return render(request, 'book_performer.html', context)
