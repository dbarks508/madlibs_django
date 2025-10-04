from django import forms

class word_form(forms.Form):
    noun = forms.CharField()
    adj_1 = forms.CharField()
    adj_2 = forms.CharField()
    verb_past_tense = forms.CharField()
    famous_person = forms.CharField()
    location = forms.CharField()
    exclamation = forms.CharField()