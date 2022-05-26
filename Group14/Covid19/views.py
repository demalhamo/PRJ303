from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Covid19/index.html')

def cases(request):
    return render(request, 'Covid19/cases.html')

def prediction(request):
    return render(request, 'Covid19/prediction.html')