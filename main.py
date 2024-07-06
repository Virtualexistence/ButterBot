from typing import Final, Literal
import os, datetime
from dotenv import load_dotenv
from discord import Intents, Client, Message, File, Embed, app_commands
from discord.ext import commands, tasks
from responses import get_response, get_weekday_index
import logging

def run(TOKEN):
    intents: Intents = Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    logging.basicConfig(filename='bot_report.log',
                        level=logging.WARN,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    @bot.event
    async def on_ready():
        logging.info(f"{bot.user} is online!")
        print(f"Script initiated. {bot.user} is now online")

    @bot.command(
            alises=['hi']
    )
    async def hello(ctx):
        """ A simple hello ;)"""
        await ctx.send("Hello!")

    @bot.hybrid_command()
    async def schedule(ctx, time, day:Literal['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri']):
        """ Schedule a meeting at given time and day"""
        try:
            day_idx = get_weekday_index(day)
            assert day_idx > -1
            check_time.start(ctx, time, get_weekday_index(day))
            await ctx.send(f'''Time-zone: IST \nScheduled the call at {time} on {day}. Recorded at {datetime.datetime.now()}''')
        except AssertionError:
            ctx.send("Error in day")
        except:
            await ctx.send("Error! Call already scheduled.")

    @bot.hybrid_command()
    async def sync(ctx):
        logging.info("sync command")
        if ctx.author.id == int(os.getenv("OWNER_USERID")):
            await bot.tree.sync()
            await ctx.send('Command tree synced.')
        else:
            await ctx.send('You must be the owner to use this command!')

    @bot.command()
    async def say(ctx, *data):
        await ctx.send(" ".join(data))

    @bot.hybrid_command()
    async def cancel_call(ctx):
        '''Cancel the call'''
        check_time.stop()
        await ctx.send("Call has been cancelled.")

    @bot.hybrid_command()
    async def pass_me_butter(ctx):
        '''Get some butter'''
        await ctx.send(content="Here's you butter", file=File('assets/images/butter.png'))
        
    @tasks.loop(minutes=1)
    async def check_time(channel, ping_time, weekday):
        now = datetime.datetime.now().strftime("%H:%M")
        if now == ping_time:
            logging.info(f"Meeting announcement sent to channel at {now}")
            await channel.send("@everyone, Let's Check in!")

    bot.run(token=TOKEN)

if __name__ == '__main__':
    load_dotenv()
    run(os.getenv("DISCORD_TOKEN"))
