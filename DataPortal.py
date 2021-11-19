import pandas as pd
import urllib.request
import urllib.parse as urlparse
import requests
import xmltodict
from pandas import json_normalize 

class DataportalApi():
    def __init__(self, url,serviceKey):
        self.url = url
        self.serviceKey = serviceKey
        self.response = None
        self.dataframe = pd.DataFrame()
        
        

    def get_request_query(self, operation, params):
        params = urlparse.urlencode(params)
        request_query = f'{self.url}/{operation}?serviceKey={self.serviceKey}&{params}'
        self.response = requests.get(url = request_query)
    
    def parse_response(self):
        if self.response.ok:
            content = self.response.content
            box = xmltodict.parse(content)
            temp = json_normalize(box['response']['body'])
            self.dataframe = pd.concat([self.dataframe, temp])
            
        return self.dataframe

if __name__ == '__main__':

    url = 'http://apis.data.go.kr/1360000/WthrChartInfoService'
    serviceKey = 'Test'
    dataportal = DataportalApi(url, serviceKey)

    operation = 'getSurfaceChart'
    params = {'code' : 12, 'time' : '20211118'} 
    response = dataportal.get_request_query(operation, params)
    api_out = dataportal.parse_response()
    print(api_out.head())