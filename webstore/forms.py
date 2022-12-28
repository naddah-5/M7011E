from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from webstore.models import UserProfile, Product

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')
        error_messages = {
            'username': {
                'unique': "That user name is already in use",
            }
        }

        def save(self, commit=True):
            """
            Verifies that the given data is valid then saves the new user into the db.
            """
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
                UserProfile.objects.create(user=user)
            return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'thumbnail']

class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', )

