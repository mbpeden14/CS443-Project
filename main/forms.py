from django import forms
from .import models

class NewFeedBatchForm(forms.ModelForm):

    class Meta:
        model = models.FeedBatch
        fields = ['dairy_cow_group', 'beef_cow_group', 'chicken_group', 'goat_group', 'pig_group']