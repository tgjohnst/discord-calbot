# discord-calbot
A simple discord bot to poll scheduled events on a server/guild, convert them to ics, and push that ics to a consistent place

## Approach
The scope of this bot is simply to maintain a consistently-updated ics file that guild members can subscribe to so that events appear on their calendar of choice with the correct time and description. At the time of its initial design, there is no intent to build in functionality for pushing calendar events back to discord, outputting to any other formats besides ics, filtering for specific subsets of events, etc.

The bot will run in python, using a client-polling approach and function wrappers. It will be hosted on (???). ical files will be output to (???) using (???).


## Requirements
- python 3.10
- discord.py (https://discordpy.readthedocs.io/en/stable/)
- ics.py (https://icspy.readthedocs.io/en/stable/)

## Helpful references
https://realpython.com/how-to-make-a-discord-bot-python/
