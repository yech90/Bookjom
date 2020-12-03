from django.shortcuts import render, redirect
from django.urls import resolve, reverse
from django.utils import translation
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings as conf_settings
from django.utils.translation import gettext as _
from .forms import contactForm
import logging
from .models import Portfolio

# Create your views here.
logger = logging.getLogger(__name__)

def showBooks(request):
    portfolios = Portfolio.objects.all()
    for portfolio in portfolios:
        portfolio.title=_(portfolio.title)
        portfolio.label=_(portfolio.label)
        portfolio.main_detail=_(portfolio.main_detail)
        portfolio.second_detail=_(portfolio.second_detail)
        
    return render(request, 'index.html', {'portfolios':portfolios})

def set_language_from_url(request, user_language):
    if user_language == conf_settings.LANGUAGE_CODE:
        redirect_path = '/'
    else:
        redirect_path = f'/{user_language}/'
    translation.activate(user_language)
    response = HttpResponseRedirect(redirect_path)
    response.set_cookie(conf_settings.LANGUAGE_COOKIE_NAME, user_language)
    return response


def contactView(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            tel = form.cleaned_data['tel']
            subject = "[yech portfolio] from "+name
            body = "Name : " + name + "\n"
            body += "email : "+ email + "\n"
            body += "tel : " + tel + "\n"
            body += "message : " + message
            recipients = [ conf_settings.EMAIL_HOST_USER]
            send_mail(subject, body, email, recipients, fail_silently=False)
            return render(request, 'index.html')
    else:
        form = contactForm()
    return render(request, 'index.html')

