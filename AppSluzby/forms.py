from django import forms

from .models import Person,PersonOnCeremony,PersonOnDuty,Ceremony,Duty

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields = ('name','surname',)

class DutyForm(forms.ModelForm):
    class Meta:
        model=Duty
        fields = ('typeOfDuty','date')

class PersonOnDutyForm(forms.ModelForm):
    class Meta:
        model = PersonOnDuty
        fields = ('idPerson','idDuty')

class CeremonyForm(forms.ModelForm):
    class Meta:
        model = Ceremony
        fields = ('nameOfCeremony','date','duration')

class PersonOnCeremonyForm(forms.ModelForm):
    class Meta:
        model = PersonOnCeremony
        fields = ('idPerson','idCeremony')