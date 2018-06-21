from django.shortcuts import render
from .proj import ContactForm

def home(request):
    if request.method == 'post':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})