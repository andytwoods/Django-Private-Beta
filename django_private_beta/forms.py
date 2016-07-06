from __future__ import unicode_literals
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from models import PrivateBetaModel

#code mostly from django.accounts

class PrivateBetaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PrivateBetaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('email', placeholder="Enter Email", autofocus=""),
            Field('name', placeholder="Enter Full Name"),

            Submit('submit', 'Submit', css_class="btn-warning"),
            )

    class Meta:
        model = PrivateBetaModel
        fields = "__all__"
