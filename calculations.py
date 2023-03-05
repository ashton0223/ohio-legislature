import datetime
import math

def get_session_number():
    now = datetime.datetime.now().year

    # Sessions last for two years
    session = math.ceil((now - 1754) / 2)
    session_int = int(session)

    return session_int