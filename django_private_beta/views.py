from __future__ import unicode_literals
from braces import views as bracesviews
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from models import PrivateBetaModel
from . import forms
from django.shortcuts import render

class PrivateBeta(bracesviews.AnonymousRequiredMixin,
                 bracesviews.FormValidMessageMixin,
                 generic.CreateView):

    form_class = forms.PrivateBetaForm
    model = PrivateBetaModel
    template_name = 'private_beta/private_beta.html'
    success_url = reverse_lazy('home')
    form_valid_message = "You've logged your interest and will get an invite first thing."

    def form_valid(self, form):
        r = super(PrivateBeta, self).form_valid(form)
        name = form.cleaned_data["email"]
        email = form.cleaned_data["name"]
        PrivateBetaModel.objects.create(name=name, email=email).save()
        return r


def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'index.html', {'form': forms.PrivateBetaForm()})