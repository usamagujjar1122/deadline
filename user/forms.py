from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'required':'',
            'name':'username',

            'type':'text',
            'placeholder':'John Doe',
            'maxlength': '16',
            'minlength': '6',
            })





    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
