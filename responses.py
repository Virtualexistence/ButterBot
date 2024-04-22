from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return "Well you're silent"
    elif 'hello' in lowered:
        return "Hello!"
    elif 'bye' in lowered:
        return "See ya!"
    else:
        return "I don't understand what you're saying"