from django import forms


class BoardNewPost(forms.Form):
    text = forms.CharField(widget=forms.Textarea)