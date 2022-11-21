from django import forms
from .import models

class NewFeedBatchForm(forms.ModelForm):
    class Meta:
        model = models.FeedBatch
        fields = ['dairy_cow_group', 'beef_cow_group', 'chicken_group', 'goat_group', 'pig_group']

class NewIngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = ['name']

class NewBeefCowGroupForm(forms.ModelForm):
    class Meta:
        model = models.BeefCowGroup
        fields = ['name', 'average_meat_output']

class NewDairyCowGroupForm(forms.ModelForm):
    class Meta:
        model = models.DairyCowGroup
        fields = ['name', 'average_milk_production']

class NewChickenGroupForm(forms.ModelForm):
    class Meta:
        model = models.ChickenGroup
        fields = ['name', 'average_meat_output']

class NewGoatGroupForm(forms.ModelForm):
    class Meta:
        model = models.GoatGroup
        fields = ['name', 'average_milk_production']

class NewPigGroupForm(forms.ModelForm):
    class Meta:
        model = models.PigGroup
        fields = ['name', 'average_meat_output']