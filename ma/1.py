import requests
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
load_dotenv(verbose=True)

API_KEY = os.getenv('API_KEY') #키는 숨기기
LAWD_CD="36110"
DEAL_YMD="202012"
url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent?serviceKey={}&LAWD_CD=36110&DEAL_YMD=202012".format(API= API_KEY)
rq = requests.get(URL)
soup = BeautifulSoup(rq.text, "html.parser") 