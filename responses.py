from random import choice, randint
from datetime import datetime


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    yt_link = 'https://www.youtube.com/watch?v=UYJDKSah-Ww'
    butter_link = 'assets/images/butter.png'

    if lowered == '':
        return "Well you're silent"
    elif 'hello' in lowered:
        return "Hello!"
    elif 'bye' in lowered:
        return "See ya!"
    elif "tutorial" in lowered:
        return f"Here's YT link to get started: {yt_link}"
    elif 'butter' in lowered:
        return "Here's your butter: ", butter_link
    elif 'purpose' in lowered:
        return 'https://tenor.com/en-IN/view/butter-robot-gif-21973199'
    elif 'ping' in lowered:
        return "@everyone"
    elif 'schedule' in lowered:
        dis_time = datetime.now()
        return str(dis_time.hour) +" "+ str(datetime.weekday(dis_time))
    else:
        return "I don't understand what you're saying", 0, 0