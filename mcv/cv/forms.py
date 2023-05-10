from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    phone_number = forms.CharField(label='Numer telefonu')
    mail = forms.EmailField(label='Email')
    address = forms.CharField(label='Adres')
    photo = forms.FileField(label='Zdjęcie')

class ExpForm(forms.Form):
    time = forms.CharField(label='Okres zatrudnienia')
    exp = forms.CharField(max_length=200, label ='Stanowisko')

class EduForm(forms.Form):
    school_time = forms.CharField(label='Czas trwania')
    school = forms.CharField(max_length=200, label ='Szkoła')

    
