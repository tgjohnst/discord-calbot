import json
import os
import asyncio
import aiohttp
import ics

from dotenv import load_dotenv

class ScheduledEvents:
    """Class connected to discord endpoint via http to communicate with it.
    """
    
    GUILD_ONLY = 2
    STAGE_INSTANCE = 1
    VOICE = 2
    EXTERNAL = 3
    
    load_dotenv()
    TOKEN:str = os.getenv('DISCORD_TOKEN')
    GUILD:int = os.getenv('DISCORD_GUILD')
    CLIENT_ID:int = os.getenv('DISCORD_CLIENT_ID')
    BOT:str = "https://discord.com/oauth2/authorize?client_id=" + str(CLIENT_ID)
    API_URL:str = "https://discord.com/api/v8"
    
    AUTH_HEADERS:dict = {
        "Authorization":f"Bot {TOKEN}",
        "User-Agent":f"DiscordBot ({BOT}) Python/3.10 aiohttp/3.8.1",
        "Content-Type":"application/json"
    }
    
    @staticmethod
    async def list_guild_events(guild_id:int)->list:
        """Returns a list of upcoming events for the supplied guild ID
        Format of return is a list of one dictionary per event containing information.
        Args:
            guild_id (int): Guild id in the endpoint
        Returns:
            list: Events as objects
        """
        
        ENDPOINT_URL = f"{ScheduledEvents.API_URL}/guilds/{guild_id}/scheduled-events"
        
        async with aiohttp.ClientSession(headers=ScheduledEvents.AUTH_HEADERS) as session:
            try:
                async with session.get(ENDPOINT_URL) as response:
                    response.raise_for_status()
                    assert response.status == 200
                    response_list = json.loads(await response.read())
            except Exception as e:
                print(f"EXCEPTION: {e}")
            finally:
                await session.close()
        return response_list
                
                
async def test():
    abc = await ScheduledEvents.list_guild_events(907946271946440745)
    abc = json.dumps(abc, indent=2)
    print(abc)
    
    
if __name__ == "__main__":
    """In case of trying to execute this module, nothing should happen.
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())