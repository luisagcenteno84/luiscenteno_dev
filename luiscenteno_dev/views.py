from django.shortcuts import render

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