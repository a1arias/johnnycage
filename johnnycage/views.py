from django.shortcuts import render
from johnnycage.models import Page

def index(request):
    p = Page.objects.get(name__iexact='home')

    return render(request, 'johnnycage/index.html',
                  {'page': p})
