from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    # return HttpResponse('<h1>Welcome</h1>')
    return render(request, 'score_predictor/index.html')

def form(request):
    return render(request, 'score_predictor/form_predict.html')