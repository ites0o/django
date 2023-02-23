from django import forms


# create a user registration form
class UserRegForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    id_number = forms.CharField()
    date_of_birth = forms.CharField()
    password = forms.CharField()


class MembersReg(forms.Form):
    name = forms.CharField(max_length=100)
    user_password = forms.CharField()

class MembersReg(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

