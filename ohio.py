import requests
import json
import calculations

URL = "https://search-prod.lis.state.oh.us"
SESSION_ENDPOINT = "/solarapi/v1/general_assembly_"
#/solarapi/v1/general_assembly_"
HEADERS = {'User-Agent': 'python'}

class Ohio:
    def __init__(self):
        pass

def request_ohio(directory):
    url = f'{URL}{directory}?format=json'
    res = requests.get(url, headers=HEADERS)
    data = json.loads(res.text)
    return data

def get_session_endpoint():
    session_number = calculations.get_session_number()
    endpoint = f'{SESSION_ENDPOINT}{session_number}'
    return endpoint

if __name__ == "__main__":
    session_endpoint = get_session_endpoint()
    session_data = request_ohio(session_endpoint)
    print(session_data["bills"])