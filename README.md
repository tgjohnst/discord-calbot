# discord-calbot
A simple Discord bot to poll scheduled events on a server/guild, convert them to ics, and push that ics to a consistent place.

### 4/22/24: This project was never completed due to lack of implementation of the scheduled events API at the time I worked on it. Perhaps I'll come back to it in the future.

## Approach
The scope of this bot is simply to maintain a consistently-updated ics file that guild members can subscribe to so that events appear on their calendar of choice with the correct time and description. At the time of its initial design, there is no intent to build in functionality for pushing calendar events back to discord, outputting to any other formats besides ics, filtering for specific subsets of events, etc.

The bot will run in python, using a client-polling approach and function wrappers. It will be hosted on (???). ical files will be output to (???) using (???).

*Unfortunately, the scheduled events API is not fully implemented in discord.py, so there is no way to call the `list_scheduled_events` endpoint within that framework. We do that manually, following the example set by the Barmaid bot (see references below) and use discord.py for the rest of the bot functionality*

## Requirements
This bot was written with Python 3.10, and requires at least Python 3.7+. See requirements.txt for all other dependencies.

# Installation and use
`pip install -r requirements.txt`

\#TODO

## Helpful references
https://realpython.com/how-to-make-a-discord-bot-python/

https://github.com/Fortex365/Barmaid/blob/main/barmaid/scheduled_events.py

