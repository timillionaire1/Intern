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


class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response (serializer.data)
    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
