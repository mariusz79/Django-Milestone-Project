from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

email_address = settings.EMAIL_HOST_USER



def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, [email_address])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('email')
    return render(request, "contact.html", {'form': form})


def contact_success(request):
    return render(request, "contact_success.html")