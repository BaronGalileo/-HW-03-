from django import forms


from .models import MyText


class PostForm(forms.ModelForm):


    class Meta:
        model = MyText
        fields = ('text', 'count')











class Wordcount(forms.ModelForm):
    class Meta:
        model = MyText
        fields = ('count',)

