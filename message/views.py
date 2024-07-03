from django.shortcuts import render, redirect

from message.forms import ContactMessageForm
# Create your views here.
from message.models import ContactMessage


def index(request):
    messages = ContactMessage.objects.all()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adushi')

    ctx = {
        'messages': messages,
        'form': ContactMessageForm()
    }

    return render(request, 'message/index.html', ctx)


def adushi(request):
    return render(request, 'message/blag.html')