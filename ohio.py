import requests
import json
import calculations

URL = "https://search-prod.lis.state.oh.us/solarapi/v1/general_assembly_"
HEADERS = {'User-Agent': 'python'}

def request_ohio(session, directory=""):
    url = f'{URL}{session}{directory}?format=json'
    res = requests.get(url, headers=HEADERS)
    data = json.loads(res.text)
    return data

def get_endpoint(year):
    return f'{URL}{year}'

if __name__ == "__main__":
    session = calculations.get_session_number()
    print(request_ohio(session))