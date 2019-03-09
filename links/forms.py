from django import forms

from . import models

class LinkForm(forms.ModelForm):
    class Meta:
        model = models.Link
        fields = [
            "title",
            "description",
            "category",
            "link",
            "nsfw",
        ]


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            "comment",
            # "rating",
        ]


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
