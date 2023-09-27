from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import MyForm

from .models import Snippet
from .serializers import SnippetSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


def home(request):
    if request.method == 'POST':
        details=MyForm(request.POST)
        if details.is_valid():
            details.save()
            return HttpResponse("data has been submitted")
        else:
            template = loader.get_template('text.html')
            return HttpResponse(template.render())
            # return render(request, 'text.html')
    else:
        details=MyForm()
        context={
            'form':details
        }
        return render(request, 'text.html', context)
