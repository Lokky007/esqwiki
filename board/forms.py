from django import forms


class BoardNewPost(forms.Form):
    text = forms.CharField(required=True, label="", widget=forms.Textarea(attrs={'rows': 2, 'cols': 50}))
