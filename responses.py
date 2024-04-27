from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    yt_link = 'https://www.youtube.com/watch?v=UYJDKSah-Ww'
    butter_link = 'assets/images/butter.png'

    if lowered == '':
        return "Well you're silent"
    elif 'hello' in lowered:
        return "Hello!", 0, 0
    elif 'bye' in lowered:
        return "See ya!", 0, 0
    elif "tutorial" in lowered:
        return f"Here's YT link to get started: {yt_link}", 0, 0
    elif 'pass the butter':
        return "Here's your butter: ", butter_link, 2
    else:
        return "I don't understand what you're saying", 0, 0