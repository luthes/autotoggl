#!/usr/bin/python
from TogglPy import Toggl
import random
import datetime
import sys
import argparse

# Get Toggl API key from File
with open('.logininfo') as f:
    creds = str(f.readline())

# Create Toggl Object
toggl = Toggl()
toggl.setAPIKey(creds.strip())
response = toggl.request("https://www.toggl.com/api/v8/clients")

def print_clients():
    response = toggl.request("https://www.toggl.com/api/v8/clients")
    print(response)

# This will add a record for the currnet day that starts at 10, and is an
# 8 hour duration
def daily_record():
    if datetime.datetime.today().weekday() not in (4, 5):
        toggl.createTimeEntry(hourduration=random.triangular(8, 10, 9.5), \
                projectid='11578007', \
                description='Data Science and Elastic Beanstalk',
                )
    else:
        print('Why are you working? It\'s the weekend!')

# This should fill in missing entries with an hour that's about 9 hours.
# Perhaps the range should be a list of dates, rather than a range.
# Add a check for Weekends.
def fill_missing(begin, end, descrip):
    for day in range(begin, end):
        toggl.createTimeEntry(hourduration=random.triangular(8, 10, 9.5), \
                projectid='11578007', \
                description=descrip, \
                day=day, \
                hour=5, \
                minute=random.randint(20,55), \
                )

def main():
    daily_record()
    return

if __name__ == "__main__":
    main()

## Automate missing time entries!
#for day in (29, 30, 31):
#	toggl.createTimeEntry(hourduration=9, projectname='someproject', day=day, hour=10)
#
