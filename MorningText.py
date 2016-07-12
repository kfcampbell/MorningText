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
# url_string = "http://gd2.mlb.com/components/game/mlb/year_" + year_string + "/month_" + month_string + "/day_" + day_string + "/master_scoreboard.json"

# get the information
# response = urllib2.urlopen(url_string)
# data = json.load(response)

# dummy practice for processing. remove later.
url_string = "http://gd2.mlb.com/components/game/mlb/year_2016/month_07/day_15/master_scoreboard.json"
response = urllib2.urlopen(url_string)
data = json.load(response)

# process the information. NEEDS TO BE IMPLEMENTED! 
# print data["data"]
data_one = data["data"]
games = data_one["games"] # going to need a for loop here in the future to search for the M's games.
game_one = games["game"]

for game in game_one:
    if game["away_team_name"] == "Mariners" or game["home_team_name"] == "Mariners":
        print "M's are playing today!"

    game_string = game["away_team_name"] + " at " + game["home_team_name"]
    away_pitcher = game["away_probable_pitcher"]
    home_pitcher = game["home_probable_pitcher"]
    away_pitcher_stats = ""
    home_pitcher_stats = ""
    

    # construct the pitcher names
    
    # now check to see if there's a pitcher announced yet
    if not away_pitcher["last"]:
        away_pitcher_name = "Unannounced"
    else:
        away_pitcher_name = away_pitcher["first"] + " " + away_pitcher["last"]
        away_pitcher_stats = " (" + away_pitcher["s_wins"] + "-" + away_pitcher["s_losses"] + ", " + away_pitcher["s_era"] + ") "

    if not home_pitcher["last"]:
        home_pitcher_name = "Unannounced"
    else:
        home_pitcher_name = home_pitcher["first"] + " " + home_pitcher["last"]
        home_pitcher_stats = " (" + home_pitcher["s_wins"] + "-" + home_pitcher["s_losses"] + ", " + home_pitcher["s_era"] + ") "


    pitcher_string = "Pitching matchup: " + away_pitcher_name + away_pitcher_stats + " vs. " + home_pitcher_name + home_pitcher_stats
    print game_string
    print pitcher_string

# construct the message. this is an example that needs to be changed to actual data once the All-Star break is over.
home_pitcher = "Iwakuma"
away_pitcher = "Some loser"
game_time = "7:10pm"
body = "The Mariners game today is at " + game_time + ". Probable starters: " + away_pitcher + " vs. " + home_pitcher + "."


# send the message
client = TwilioRestClient(account_sid, auth_token)
# message = client.messages.create(body=body, to=keegan_number, from_=from_number)
