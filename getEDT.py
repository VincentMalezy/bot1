import requests as requests
from icalendar import Calendar
from datetime import date, timedelta

def getCours():
    # icalfile = open('edt.ics', 'rb')
    # gcal = Calendar.from_ical(icalfile.read())

    url = "http://edt-v2.univ-nantes.fr/calendar/ics?timetables[0]=52637"
    gcal = Calendar.from_ical(requests.get(url).text)
    liste = []

    for component in gcal.walk():
         if component.name == "VEVENT":
            liste.append(component)
        #     summary = component.get('summary')
        #     description = component.get('description')
        #     location = component.get('location')
        #     startdt = component.get('dtstart').dt
        #     enddt = component.get('dtend').dt
        #     exdate = component.get('exdate')
        #     print("{0}-{1} {2}: {3} - {4}\n".format(startdt.strftime("%D %H:%M UTC"), enddt.strftime("%D %H:%M UTC"), summary, description, location))


    today = date.today()
    tomorrow = today+timedelta(days=1)

    cours = []


    for l in liste:
        start =  l.get('DTSTART')
        if tomorrow.year ==  start.dt.year:
            if tomorrow.month ==  start.dt.month:
                if tomorrow.day == start.dt.day:
                    cours.append(l)

    return cours