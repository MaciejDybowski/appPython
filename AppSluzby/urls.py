from django.conf.urls import url
from AppSluzby import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^addPerson/$', views.addPerson, name='addPerson'),
    url(r'^addDuty/$', views.addDuty, name='addDuty'),
    url(r'^addCeremony/$', views.addCeremony, name='addCeremony'),
    url(r'^addTo/$', views.addToDuty, name='addToDuty2'),
    url(r'^addPersonToCeremony/$', views.addPersonToCeremony, name='addPersonToCeremony'),


    url(r'^ceremony/$', views.CeremonyHomePage.as_view()),
    url(r'^dashboard/$', views.DashboardHomePage.as_view()),
    url(r'^details/(?P<id>[0-9]+)/', views.DetailsPage, name='details'),
    url(r'^detailsCeremony/(?P<id>[0-9]+)/', views.DetailsPageCeremony, name='detailsCeremony'),
]