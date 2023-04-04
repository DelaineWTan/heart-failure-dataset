from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView


def homePageView(request):
    return render(request, 'home.html')


def predictPageView(request):
    return render(request, 'predict.html')


def resultsPageView(request):
    return render(request, 'results.html')
