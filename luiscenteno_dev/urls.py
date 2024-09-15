"""
URL configuration for luiscenteno_dev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('careerbot/', views.careerbot, name='careerbot'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('leaderbot/', views.leaderbot, name='leaderbot'),
    path('chat-with-documents/', views.chat_with_documents, name='chatwithdocuments'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


