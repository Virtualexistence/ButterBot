from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    yt_link = 'https://www.youtube.com/watch?v=UYJDKSah-Ww'

    if lowered == '':
        return "Well you're silent"
    elif 'hello' in lowered:
        return "Hello!"
    elif 'bye' in lowered:
        return "See ya!"
    elif "tutorial" in lowered:
        return f"Here's YT link to get started! {yt_link}"
    else:
        return "I don't understand what you're saying"