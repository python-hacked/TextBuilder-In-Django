from django.shortcuts import render, redirect
from .models import TransformedText



def index(request):
    return render(request, "index.html")



def transform_text(request, transformation):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        transformed_text = ''

        if transformation == 'uppercase':
            transformed_text = text.upper()
        elif transformation == 'lowercase':
            transformed_text = text.lower()
        elif transformation == 'clear':
            TransformedText.objects.all().delete()

        TransformedText.objects.create(text=transformed_text)

        return redirect('/home/')

def home(request):
    transformed_texts = TransformedText.objects.all().order_by('-id')[:10]
    return render(request, 'text.html', {'transformed_texts': transformed_texts})
