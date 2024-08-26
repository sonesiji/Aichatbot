# views.py
from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

# Configure API key
api_key = "AIzaSyCBHJzNyEhusj_bDljUkTvKYQU95hgcDag"
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_text(request):
    if request.method == 'POST':
        user_input = request.POST.get('input_text', '')
        if user_input:
            try:
                # Call generate_content
                response = model.generate_content(user_input)
                # Access the text directly if it's an attribute
                generated_text = response.text if hasattr(response, 'text') else 'No text found'
                return JsonResponse({'generated_text': generated_text})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'No input text provided'}, status=400)
    return render(request, 'generate_text.html')


