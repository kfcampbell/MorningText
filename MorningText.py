#!/usr/local/bin/python

import datetime
import urllib2
import json
from twilio.rest import TwilioRestClient
from keys import account_sid, auth_token, from_number, keegan_number

# get the correct date information
now = datetime.datetime.now()

# make each value a string
year_string = str(now.year)
month_string = str(now.month)
day_string = str(now.day)

# untested! # if we need to prepend a 0
if now.day < 10: 
    day_string = "0" + day_string
if now.month < 10:
    month_string = "0" + month_string

# construct the big url we need
url_string = "http://gd2.mlb.com/components/game/mlb/year_" + year_string + "/month_" + month_string + "/day_" + day_string + "/master_scoreboard.json"

# get the information
response = urllib2.urlopen(url_string)
data = json.load(response)

# process the information. NEEDS TO BE IMPLEMENTED! 
# print data["data"]
data_one = data["data"]
games = data_one["games"] # going to need a for loop here in the future to search for the M's games.
print games["game"]

# construct the message. this is an example that needs to be changed to actual data once the All-Star break is over.
home_pitcher = "Iwakuma"
away_pitcher = "Some loser"
game_time = "7:10pm"
body = "The Mariners game today is at " + game_time + ". Probable starters: " + away_pitcher + " vs. " + home_pitcher + "."


# send the message
client = TwilioRestClient(account_sid, auth_token)
# message = client.messages.create(body=body, to=keegan_number, from_=from_number)
