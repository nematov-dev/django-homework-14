from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView,CreateView
from django.utils.translation import gettext_lazy as _

from pages import forms
from pages import models

def main_page_view(request):
    return render(request,'index.html')

def home_page_view(request):

    if request.path == '/en/home/' or '/uz/home/':
        header_type = 'home_header'
    else:
        header_type = 'default_header'
    
    return render(request, 'pages/home.html', {'header_type': header_type})



class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["posts"] = models.AboutModel.objects.all()
        return context


class ContactCreateView(CreateView):
    template_name = 'pages/contact.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy('pages:contact')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request,_('Your message send succesfull'))
        return super().form_valid(form)
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        for error in form.errors:
            messages.error(self.request,error)
        return super().form_invalid(form)