## Django Rest Framework backend for Accessing google calendar events using OAuth mechanism.

To run project -> 

```sh
pip install - r requriments.txt
```

- Endpoints:
  Step 1 of OAuth, select google account
```
/rest/v1/calendar/init/ -> GoogleCalendarInitView()
```


 1. Exchange code for token  
2. Get accesstoken, get list of events
```
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
```

## Important
``` 
You'll need to create account on Google Cloud Console(needs google account), and mention your email in testers as this app is not deployed.
```
