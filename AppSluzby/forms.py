from django import forms

from .models import Person,PersonOnCeremony,PersonOnDuty,Ceremony,Duty

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        labels = {
            "degree":"Stopień",
            "name":"Imię",
            "surname":"Nazwisko"
        }
        widgets = {
            'degree': forms.TextInput(attrs={'placeholder': 'st.szer. pchor.'}),
            'name': forms.TextInput(attrs={'placeholder': 'Jan'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Kowalski'}),
        }
        fields = ('degree','name','surname',)

class DutyForm(forms.ModelForm):

    class Meta:
        test = Duty.objects.all()
        model=Duty
        labels = {
            "typeOfDuty": "Typ",
            "date": "Data",

        }
        widgets = {
            'date': forms.TextInput(attrs={'placeholder': 'Format = 2020-07-31'}),
        }
        fields = ('typeOfDuty','date')

class PersonOnDutyForm(forms.ModelForm):
    class Meta:
        model = PersonOnDuty
        labels = {
            "idPerson": "ID osoby",
            "idDuty": "ID służby",

        }

        fields = ('idPerson','idDuty')

class CeremonyForm(forms.ModelForm):
    class Meta:
        model = Ceremony
        labels = {
            "nameOfCeremony": "Nazwa",
            "date": "Data",
            "duration":"Czas trwania (n.n)"

        }
        widgets = {
            'nameOfCeremony': forms.TextInput(attrs={'placeholder': 'Defilada 3 maja'}),
            'date': forms.TextInput(attrs={'placeholder': 'Format = 2020-07-31'}),
        }
        fields = ('nameOfCeremony','date','duration')

class PersonOnCeremonyForm(forms.ModelForm):
    class Meta:
        model = PersonOnCeremony
        labels = {
            "idPerson": "ID osoby",
            "idCeremony": "ID uroczystości",

        }
        fields = ('idPerson','idCeremony')