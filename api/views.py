from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect

from google_auth_oauthlib.flow import InstalledAppFlow, Flow
import googleapiclient.discovery


@api_view(['GET'])
def getData(request):
    # redirect to /rest/v1/calendar/init
    return redirect('/rest/v1/calendar/init/')


@api_view(['GET'])
def GoogleCalendarRedirectView(request):
    secrets_file = './client_secret.json'
    scopes = ['https://www.googleapis.com/auth/calendar']
    redirect_uri = 'https://convinbackendtask.geekgaurav.repl.co/rest/v1/calendar/redirect/'
    state = request.query_params.get('state')

    flow = Flow.from_client_secrets_file(secrets_file,
                                         scopes,
                                         state=state,
                                         redirect_uri=redirect_uri)

    code = request.query_params.get('code')
    flow.fetch_token(code=code)

    credentials = flow.credentials
    service = googleapiclient.discovery.build('calendar',
                                              'v3',
                                              credentials=credentials,
                                              static_discovery=False)

    # Get the user's events from the calendar API
    events_result = service.events().list(calendarId='primary',
                                          maxResults=10,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    # Render the events in the response
    return Response(events)


@api_view(['GET'])
def GoogleCalendarInitView(request):
    # Set up the OAuth flow
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/calendar'],
        redirect_uri=
        'https://convinbackendtask.geekgaurav.repl.co/rest/v1/calendar/redirect/'
    )

    # Generate the authorization URL and redirect the user to the consent screen
    auth_url, state = flow.authorization_url(prompt='consent')
    request.session['state'] = state

    return HttpResponseRedirect(auth_url)
