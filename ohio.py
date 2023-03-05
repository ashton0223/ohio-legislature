import requests
import json
import calculations

class Ohio:
    def __init__(self, base_url, init_endpoint, headers, session=None):
        self.base_url = base_url
        self.headers = headers
        self.session = session
        self.endpoints = {"init" : init_endpoint}

    def request(self, directory):
        url = f'{self.base_url}{directory}?format=json'
        res = requests.get(url, headers=self.headers)
        data = json.loads(res.text)
        return data

    def init(self, select_session=False):
        if not select_session:
            self.session = calculations.get_session_number()
    
        if self.session is None:
            self.session = calculations.get_session_number()

        init_endpoint = f'{self.endpoints["init"]}{self.session}'
        
        self.endpoints["init"] = init_endpoint
        
        data = self.request(init_endpoint)

        self.endpoints["bills"] = data["bills"]["link"]