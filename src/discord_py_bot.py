# bot.py
from email.errors import MessageParseError
import os
import ics

import discord
from discord.ext import commands
from dotenv import load_dotenv
from scheduled_events import ScheduledEvents

#TODO drop all the following setup stuff to __main__() if we can

# Configure discord intents: Messages (respond to bot commands), scheduled events (see calendar event updates)
intents = discord.Intents(messages=True, guild_scheduled_events=True)

# Get discord auth info
load_dotenv()
TOKEN:str = os.getenv('DISCORD_TOKEN')
CLIENT_ID:str = os.getenv('DISCORD_CLIENT_ID')
CAL_ICS_URL:str = os.getenv('CALENDAR_ICS_URL')

# Commands will be of the form: "!cal {command}"
bot = commands.Bot(command_prefix='!cal ')

########################
#### Set up logging ####
########################

#TODO set up a more advanced logger
#TODO reference: https://discordpy.readthedocs.io/en/stable/logging.html

################################
#### ical utility functions ####
################################

def parse_discord_to_ical(sevent: discord.ScheduledEvent):
    raise NotImplementedError #TODO

def create_ical():
    raise NotImplementedError #TODO

def write_ical_to_s3():
    raise NotImplementedError #TODO

##########################
#### Scheduled Events ####
##########################

async def update_ical():



########################
#### Event Handlers ####
########################

# Triggered when the bot first connects
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------') #TODO make this more verbose?

# Scheduled event event handlers

@bot.event
async def on_scheduled_event_create(event):
    raise NotImplementedError #TODO

@bot.event
async def on_scheduled_event_delete(event):
    raise NotImplementedError #TODO

@bot.event
async def on_scheduled_event_update(before, after):
    raise NotImplementedError #TODO

@bot.event
async def on_scheduled_event_user_add(event, user):
    pass #TODO

@bot.event
async def on_scheduled_event_user_remove(event, user):
    pass #TODO

######################
#### Bot Commands ####
######################

# Trigger a manual calendar update
@bot.command(name='refresh', help='Trigger a manual refresh of the google calendar file. This should not be necessary.')
async def cal_refresh(ctx):
    #TODO implement this function
    response = "Updating calendar... (Not yet implemented)"
    await ctx.send(response)

# Return a link to the google calendar this will output to
@bot.command(name='link', help="Get the latest link to this server's google calendar")
async def cal_link(ctx):
    #TODO implement this function
    response = "The current link to this server's calendar is: (Not yet implemented)"
    await ctx.send(response)

bot.run(TOKEN)
