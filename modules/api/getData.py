import requests
import os


from dotenv import load_dotenv

load_dotenv(verbose=True)

api_key = os.getenv('API_KEY')
url = os.getenv('API_URL')

params = {'serviceKey': api_key, 'LAWD_CD' : '11110','DEAL_YMD':'2021312'}

response = requests.get(url,params=params)