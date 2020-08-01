import null as null
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PersonOnDuty,PersonOnCeremony,Person,Duty,Ceremony
from .forms import PersonForm, DutyForm, PersonOnDutyForm, CeremonyForm, PersonOnCeremonyForm

import xlrd


# Create your views here.
def counter(type):
    switcher = {
        'Kmp': 1,
        'Sto': 0.5,
        'Str': 1,
        'Pst': 1,
        'Bat': 1
    }
    return switcher.get(type, "Invalid input")


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        """loc = ("Pluton.xlsx")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        rows = sheet.nrows
        i = 0
        while i < rows:
            idTemp = sheet.cell_value(i, 0)
            nameTemp = sheet.cell_value(i, 1)
            surnameTemp = sheet.cell_value(i, 2)
            dutyTemp = sheet.cell_value(i,3)
            ceremonyTemp = sheet.cell_value(i,4)
            Person.objects.create(idPerson=idTemp, name=nameTemp,surname=surnameTemp,numberOfDuty=dutyTemp,
                                  numberOfCeremony=ceremonyTemp)
            i = i + 1"""

        personList = Person.objects.all()
        for i in personList:
            numberOfDuty = 0.0
            Dutys = PersonOnDuty.objects.filter(idPerson=i.idPerson)
            for p in Dutys:
                numberOfDuty += counter(p.idDuty.typeOfDuty)
            i.numberOfDuty = numberOfDuty
            i.save()


        person = Person.objects.order_by(Coalesce('numberOfDuty','surname').desc())
        best = person[:5]
        person = Person.objects.order_by(Coalesce('numberOfDuty', 'surname').asc())
        worst = person[:5]
        return render(request, 'index.html', {'best': best,'worst':worst,'all':personList})


def DetailsPage(request,id):
    person = Person.objects.get(idPerson=id)
    dutys = PersonOnDuty.objects.filter(idPerson=id)
    return render(request, 'details.html', {'person':person,'dutys':dutys})


def DetailsPageCeremony(request,id):
    person = Person.objects.get(idPerson=id)
    dutys = PersonOnCeremony.objects.filter(idPerson=id)
    return render(request, 'detailsCeremony.html', {'person':person,'dutys':dutys})

class CeremonyHomePage(TemplateView):
    def get(self, request, **kwargs):

        personList = Person.objects.all()
        for i in personList:
            numberOfDuration = 0.0
            Ceremonys = PersonOnCeremony.objects.filter(idPerson=i.idPerson)
            for p in Ceremonys:
                numberOfDuration += p.idCeremony.duration
            i.numberOfCeremony = numberOfDuration
            i.save()

        personList.order_by(Coalesce('numberOfCeremony', 'surname').desc())
        return render(request, 'ceremony.html', {'all':personList})

class DashboardHomePage(TemplateView):
    def get(self, request, **kwargs):
        return allInOne(request)

def allInOne(request):
    personForm = PersonForm()
    dutyForm = DutyForm()
    personOnDutyForm = PersonOnDutyForm()
    ceremonyForm = CeremonyForm()
    personOnCeremonyForm = PersonOnCeremonyForm()
    personList = Person.objects.all()
    dutyList = Duty.objects.all().order_by(Coalesce('idDuty', 'date').desc())
    ceremonyList = Ceremony.objects.all().order_by(Coalesce('idCeremony', 'date').desc())
    return render(request, 'dashboard.html', {'personList': personList,
                                              'ceremonyList': ceremonyList,
                                              'dutyList': dutyList,
                                              'personForm': personForm,
                                              'dutyForm': dutyForm,
                                              'personOnDutyForm': personOnDutyForm,
                                              'ceremonyForm': ceremonyForm,
                                              'personOnCeremonyForm': personOnCeremonyForm
                                              })


def addPerson(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.numberOfDuty = 0
            person.numberOfCeremony = 0
            person.save()
            return allInOne(request)
        else:
            html = '<h1>Wystapil blad</h1>'
            return HttpResponse(html)

def addDuty(request):
    if request.method == 'POST':
        form = DutyForm(request.POST)
        if form.is_valid():
            form.save()
            return allInOne(request)
        else:
            html = '<h1>Wystapil blad</h1>'
            return HttpResponse(html)


def addCeremony(request):
    if request.method == 'POST':
        form = CeremonyForm(request.POST)
        if form.is_valid():
            form.save()
            return allInOne(request)
        else:
            html = '<h1>Wystapil blad</h1>'
            return HttpResponse(html)

def addPersonToCeremony(request):
    if request.method == 'POST':
        form = PersonOnCeremonyForm(request.POST)
        if form.is_valid():
            form.save()
            return allInOne(request)
        else:
            html = '<h1>Wystapil blad</h1>'
            return HttpResponse(html)


def addToDuty(request):
    if request.method == 'POST':
        form = PersonOnDutyForm(request.POST)
        if form.is_valid():
            form.save()
            return allInOne(request)
        else:
            html = '<h1>Wystapil blad</h1>'
            return HttpResponse(html)