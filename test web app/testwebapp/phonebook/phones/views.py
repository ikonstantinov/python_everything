from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'add.html', {
        'form': form,
    })
