from django.shortcuts import render
from .forms import UserRegForm
from .forms import MembersReg


def register(request):
    register_button = request.POST.get('m-btn-reg')
    name = ''
    email = ''
    id_number = ''
    date_of_birth = ''
    password = ''
    form = UserRegForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        id_number = form.cleaned_data.get("id_number")
        date_of_birth = form.cleaned_data.get("date_of_birth")
        password = form.cleaned_data.get("password")

    context = {'form': form, 'name': name, 'email': email, 'id_number': id_number,
               'date_of_birth': date_of_birth, 'password': password,
               'register_button': register_button}
    return render(request, 'register.html', context)


def reg_members(request):
    submit_members = request.POST.get('m-btn-reg')
    name = ''
    age = ''
    phone = ''
    city = ''
    country = ''

    reg_members_form = MembersReg(request.POST or None)
    if reg_members_form.is_valid():
        name = reg_members_form.cleaned_data.get("name")
        age = reg_members_form.cleaned_data.get("age")
        phone = reg_members_form.cleaned_data.get("phone")
        city = reg_members_form.cleaned_data.get("city")
        country = reg_members_form.cleaned_data.get("country")

    context = {'reg_members_form': reg_members_form,
               'name': name,
               'age': age,
               'phone': phone,
               'city': city,
               'country': country,
               'submit_members': submit_members

               }

    return render(request, 'members.html', context)
