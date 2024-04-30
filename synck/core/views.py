from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

# Create your views here.
from .form import ContactForm


class ContactView(View):
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent")
            return redirect("home")
        messages.error(request, "Your message could not be sent")
        return redirect("home")
