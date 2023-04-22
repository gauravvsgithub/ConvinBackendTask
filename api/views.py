from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect

from google_auth_oauthlib.flow import InstalledAppFlow


@api_view(['GET'])
def getData(request):
    # redirect to /rest/v1/calendar/init
    return redirect('/rest/v1/calendar/init/')


@api_view(['GET'])
def GoogleCalendarRedirectView(request):
    item = {'message': 'Calendar Redirect View'}
    return Response(item)


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
