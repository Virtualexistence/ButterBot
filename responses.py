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
        return f"Done, scheduled. Recorded on {datetime.now()} UTC Timezone"
    elif 'cancel' in lowered:
        return "Gotcha, removed the call"
    else:
        return "I don't understand what you're saying", 0, 0
    
def get_weekday_index(in_words):
    weekday_dict={
        "monday":0,
        "tuesday":1,
        "wednesday":2,
        'thursday':3,
        "friday":4,
        "saturday":5,
        "sunday":6
    }
    in_int = weekday_dict.get(in_words)
    if isinstance(in_int, int):
        return in_int
    else:
        return -1