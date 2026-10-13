from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('cmmnt_body_txt','stars_point_prdct', )

    