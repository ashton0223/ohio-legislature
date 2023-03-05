from ohio import Ohio

URL = "https://search-prod.lis.state.oh.us"
SESSION_ENDPOINT = "/solarapi/v1/general_assembly_"
HEADERS = {'User-Agent': 'python'}

if __name__ == "__main__":
    legis = Ohio(URL, SESSION_ENDPOINT, HEADERS)
    legis.init()
    print(legis.endpoints["bills"])