from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from main.models import Pagina

def index(request):
    try:
        the_text = Pagina.objects.get(slug = 'home',)
    except ObjectDoesNotExist:
        return render(request, "404.html",{"message":"There is no active catalogue",})

    return render(request, "index.html", {'text':the_text})
