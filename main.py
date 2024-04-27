from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, File, Embed
from responses import get_response

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
        if response[1]:
            if response[2] == 1:
                await message.channel.send(content=response[0], embed=Embed(type='rich',description="Placeholder", url=response[1]))
            elif response[2] == 2:
                await message.channel.send(content=response[0], file=File(response[1]))
            else:
                await message.channel.send(file=File('assets/images/butter.png'))
        else:
            response = response[0]
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
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: {user_message}')
    await send_message(message, user_message)


def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()