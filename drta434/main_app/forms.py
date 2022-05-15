from django import forms


class AddPostForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)