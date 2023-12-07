from django import forms


class SiteCreateForm(forms.Form):
    url = forms.URLField()
