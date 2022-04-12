from django import forms
from django.forms import CharField, ModelForm
from .models import Team

class TeamForm(ModelForm):
    name = forms.CharField(max_length=20, required=True, label="", widget=forms.TextInput({'placeholder': 'Team Name'}))
    lead = forms.CharField(max_length=20, required=True, label="", widget=forms.TextInput({'placeholder': 'Team Lead'}))
    class Meta:
        model = Team
        fields = ['name', 'lead']

class Input(ModelForm):
    hunters = forms.IntegerField(required=True, label="Enter number of humans to send for hunting ", 
    widget=forms.NumberInput({'placeholder': 'Hunter Count'}))
    water_gatherers = forms.IntegerField(required=True, label="Do you want to pump water ?? It takes 2 humans per day(1/0)",
    widget=forms.NumberInput({'placeholder': 'Water Gatherer (1/0)'}))
    solar_panel_cleaner = forms.IntegerField(required=True, label="Do you want to clean the solar panels?? (1/0) It takes 1 human per day ", 
    widget=forms.NumberInput({'placeholder': 'Solar Panel Cleaner (1/0)'}))
    shelter_makers = forms.IntegerField(required=True, label="Enter number of humans for shelter making ", 
    widget=forms.NumberInput({'placeholder': 'Shelter Maker Count'}))
    weapon_makers = forms.IntegerField(required=True, label="Enter number of humans for weapon making ",
    widget=forms.NumberInput({'placeholder': 'Weapon Makers Count'}))
    miners = forms.IntegerField(required=True, label="Enter number of humans for mining ",
    widget=forms.NumberInput({'placeholder': 'Miners Count'}))
    class Meta:
        model = Team
        fields = ['hunters', 'water_gatherers', 'solar_panel_cleaner', 'shelter_makers', 
        'weapon_makers', 'miners']

class ConditionInput(ModelForm):
    explorers1 = forms.IntegerField(required=True, label="", widget=forms.NumberInput({'placeholder': 'Dice 1 Result'}))
    explorers2 = forms.IntegerField(required=True, label="", widget=forms.NumberInput({'placeholder': 'Dice 2 Result'}))
    class Meta:
        model = Team
        fields = ['explorers1', 'explorers2']

class SideQuest(ModelForm):
    sidequest = forms.IntegerField(required=True, label="", widget=forms.NumberInput({'placeholder': 'SideQuest Number'}))
    sideQres = forms.IntegerField(required=True, label="", widget=forms.NumberInput({'placeholder': 'SideQuest Result'}))
    class Meta:
        model = Team
        fields = ['sidequest', 'sideQres']