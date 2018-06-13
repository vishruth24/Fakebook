def addtocalapi(birthdays):

    from apiclient.discovery import build
    from httplib2 import Http
    from oauth2client import file, client, tools
    import datetime
    # Setup the Calendar API
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    CAL= build('calendar', 'v3', http=creds.authorize(Http()))

    GMT_OFF='+05:30'
    for k,v in birthdays.items():
        day,month=v.split('/')
        EVENT={
        'summary':'It\'s %s\'s birthday today!'% k,
        'start':{'dateTime':'2018-{}-{}T00:00:00{}'.format(month,day,GMT_OFF)},
        'end':{'dateTime':'2018-{}-{}T14:00:00{}'.format(month,day,GMT_OFF)},
        }

        e=CAL.events().insert(calendarId='primary',body=EVENT).execute()
        print(e['summary']+' added')
