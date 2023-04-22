from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect


@api_view(['GET'])
def getData(request):
    item = {'message': 'Head to /rest/v1/calendar/init/ end point'}
    return redirect('/rest/v1/calendar/init/')


@api_view(['GET'])
def GoogleCalendarRedirectView(request):
    item = {'message': 'Calendar Redirect View'}
    return Response(item)


@api_view(['GET'])
def GoogleCalendarInitView(request):
    item = {'message': 'Calendar Init View'}
    return Response(item)
