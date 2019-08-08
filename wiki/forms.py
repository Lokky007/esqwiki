# -*- coding: utf-8 -*-

from django import forms


class WikiNewRecord(forms.Form):
    name = forms.CharField(required=True, label="Název nové ingredience")
    unique_item = forms.BooleanField(required=False, label="Unikátní drop")
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 50}),
                              label="Komentář")
    image = forms.ImageField(required=False, label="Obrázek")
