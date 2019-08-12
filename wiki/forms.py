# -*- coding: utf-8 -*-

from django import forms


class WikiNewRecord(forms.Form):
    name = forms.CharField(required=True, label="Název nové ingredience")
    unique_item = forms.BooleanField(required=False, label="Unikátní drop")
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 50}),
                              label="Komentář")
    image = forms.ImageField(required=False, label="Obrázek (.jpg)")

    def clean(self):
        image_file = self.cleaned_data.get('image')
        if image_file:
            if not image_file.name.endswith(".jpg"):
                raise forms.ValidationError("Only .jpg image accepted")
        return image_file
