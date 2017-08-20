#!/usr/bin/python
from TogglPy import Toggl
import random
import datetime
import ConfigParser
import argparse

# This will add a record for the currnet day that starts at 10, and is an
# 8 hour duration
def daily_record():
    if datetime.datetime.today().weekday() not in (4, 5):
        toggl.createTimeEntry(hourduration=random.triangular(8, 9, 8.5), \
                projectid='11578007', \
                description=config_description
                )
    else:
        print('Why are you working? It\'s the weekend!')

# This should fill in missing entries with an hour that's about 9 hours.
# Perhaps the range should be a list of dates, rather than a range.
# Add a check for Weekends.
def fill_missing(begin, end):
    for day in range(begin, end):
        toggl.createTimeEntry(hourduration=random.triangular(8, 9, 8.5), \
                projectid='11578007', \
                description=config_description, \
                day=day, \
                hour=5, \
                minute=random.randint(20,55), \
                )

def main():
#    fill_missing(14, 19)
#    daily_record()

    # Get Login info from File
    config = ConfigParser.ConfigParser()
    config.read('.logininfo.cfg')
    config_api_key = config.get('Toggl', 'api_key')
    
    # Create Toggl Object
    toggl = Toggl()
    toggl.setAPIKey(config_api_key)
    response = toggl.request("https://www.toggl.com/api/v8/clients")

    # Parse Arguments
    # Arguments:
    #           Fill Missing (Start, End)
    #           Today's Entry (No arguments)
    parser = argparse.ArgumentParser(description='''Automate Toggl Entries, add
    this to a cron job with the -t flag, or fill missing entries with -f.''')

    parser.add_argument('-t', '--today',\
            default=False,\
            help='''Add entry for today, defaults to an average of 8.5 hours 
                    between 8 and 9 hours.''',\
            action='store_true')

    parser.add_argument('-f', '--fill',\
            nargs=2,\
            help='Add entry for today, defaults to an average of 8.5 hours')
    args = vars(parser.parse_args())

    if args['today'] == True:
        print('Adding Daily Entry')
        daily_record()

    if args['fill'] is not None:
        print('First Day: ' + args['fill'][0])
        print('Last Day: ' + args['fill'][1])
        fill_missing(int(args['fill'][0]), int(args['fill'][1]))
    return

if __name__ == "__main__":
    main()
