import requests
import os


from dotenv import load_dotenv

load_dotenv(verbose=True)

class getData:
    
    def __init__(self):
        api_key = os.getenv('API_KEY')
        url = os.getenv('API_URL')
    
    def getApi(self):
        params = {'serviceKey': self.api_key, 'LAWD_CD' : '11110','DEAL_YMD':'2021312'}
        response = requests.get(self.url,params=params)
        return response