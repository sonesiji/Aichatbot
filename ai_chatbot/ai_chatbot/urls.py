from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Define the root URL redirect view
def redirect_to_generate(request):
    return redirect('/chatbot/generate/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_generate),  # Redirect root URL to /chatbot/generate/
    path('chatbot/', include('chatbot.urls')),  # Include the chatbot app's URLs
]
