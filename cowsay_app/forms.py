from django import forms

class WhatDoesTheCowSayForm(forms.Form):
    text = forms.CharField(max_length=200)