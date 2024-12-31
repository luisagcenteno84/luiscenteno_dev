from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html')

def careerbot(request):
    return render(request, 'careerbot.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def blog(request):
    return render(request, 'blog.html')

def chat_with_documents(request):
    return render(request, 'chat_with_documents.html')

def ecomm(request):
    return HttpResponseRedirect('https://simple-ecommerce-836653446417.us-west1.run.app/')