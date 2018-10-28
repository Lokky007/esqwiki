# -*- coding: utf-8 -*-

from django import forms


class TradeNewSell(forms.Form):
    CHOICES=[('1', 'Prodám'),
             ('2', 'Koupím')]
    tradeType = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    user_login = forms.CharField(label='Název úctu', max_length=50)

