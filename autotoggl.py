from TogglPy import Toggl
import random
import datetime
import sys
import argparse

# Create toggl object.
toggl = Toggl()

toggl.setAPIKey('APIKEY')

def print_clients():
    response = toggl.request("https://www.toggl.com/api/v8/clients")
    print(response)

# This will add a record for the currnet day that starts at 10, and is an
# 8 hour duration
def daily_record():
    if datetime.datetime.today().weekday() not in (4,5):
        toggl.createTimeEntry(\
                hourduration=0,\
                projectname='Disney Project Skye Dev Ops'\
                hour=10\
                )
    else
        print('Why are you working? It\'s the weekend!')

# This should fill in missing entries with an hour that's about 8 hours.
# Perhaps the range should be a list of dates, rather than a range.
def fill_missing():
    for day in range(1,30)
