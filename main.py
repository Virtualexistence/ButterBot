from typing import Final
import os, datetime
from dotenv import load_dotenv
from discord import Intents, Client, Message, File, Embed
from discord.ext import commands, tasks
from responses import get_response, get_weekday_index


load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOEKN")

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty")
        return None
    
    if is_private:= user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f"{client.user} is now runnning")

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 
    if str(message.content).startswith("!"):
        username: str = str(message.author)
        user_message: str = message.content
        channel: str = str(message.channel)
        if "schedule" in user_message:
            if len(user_message.split(' ')) < 3:
                await message.author.send("The format is in 24Hrs. Syntax: !schedule HH:MM Weekday") 

            global alarm_time
            global weekday
            alarm_time = user_message.split()[1]
            weekday = get_weekday_index(user_message.split()[2].lower())

            if weekday == -1:
                await message.author.send("Check Again")    
            else:
                check_time.start()
        if "cancel" in user_message:
            check_time.stop()
        print(f'[{channel}] {username}: {user_message}')

        await send_message(message, user_message)

@tasks.loop(minutes=1)
async def check_time():
    now = datetime.datetime.now().strftime("%H:%M")
    print(now, alarm_time)
    channel = client.get_channel(int(os.getenv("CHANNEL_ID")))
    if now == alarm_time: ##UTC Timezone
        await channel.send("@everyone Let's check in!")

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()