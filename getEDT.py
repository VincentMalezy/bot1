import requests as requests
from icalendar import Calendar
from datetime import date, timedelta

def getCours(jour):

    url = "https://edt.univ-nantes.fr/sciences/g351176.ics"
    gcal = Calendar.from_ical(requests.get(url).text)
    liste = []

    for component in gcal.walk():
         if component.name == "VEVENT":
            liste.append(component)


    today = date.today()
    souhait = today+timedelta(days=1)
    souhait = souhait.strftime('%Y-%m-%d')


    cours = []

    for l in liste:
        start =  l.get('DTSTART')
        verifDate = start.dt.strftime('%Y-%m-%d')

        if souhait == verifDate:
            description = l.get('DESCRIPTION')
            infos = description.split('\n')
            remarque = str(infos[len(infos) - 2])
            if ("TP A" not in remarque) and ("TPA" not in remarque) and ("groupe 1" not in remarque):
                cours.append(l)




    return cours