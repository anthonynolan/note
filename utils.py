from datetime import datetime


def get_now():
    return datetime.now().strftime("%a %b %-d %Y %-H:%M")
