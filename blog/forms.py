from django import forms

from .models import Post, Player, Team

class ReportForm(forms.Form):
    password = forms.CharField(label='Password', max_length=10)
    title = forms.CharField(label='Title', max_length=200)
    c = forms.IntegerField(label='Complexity', max_value = 5, min_value=1)
    d = forms.IntegerField(label='Depth', max_value = 5, min_value=1)
    l = forms.IntegerField(label='Luck', max_value = 5, min_value=1)
    t = forms.IntegerField(label='Time', min_value=1)
    winners = forms.ModelMultipleChoiceField(label='Winner(s)', widget=forms.CheckboxSelectMultiple, queryset = Player.objects.all())
    losers = forms.ModelMultipleChoiceField(label='Loser(s)', widget=forms.CheckboxSelectMultiple, queryset = Player.objects.all())
