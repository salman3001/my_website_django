from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactMessageForm
from .models import ContactMessage
from django.contrib import messages
from django_htmx.http import HttpResponseLocation, retarget
from django.urls import reverse

# Create your views here.


def home(request):

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you! Your request has been recieved. we will contact you shortly.",
            )

            return HttpResponseLocation(reverse("portfolio:home"))
        else:
            return retarget(
                render(request, "portfolio/ContactForm.html", {"form": form}),
                "closest form",
            )

    else:
        form = ContactMessageForm()
        return render(request, "portfolio/home.html", {"form": ContactMessageForm})
