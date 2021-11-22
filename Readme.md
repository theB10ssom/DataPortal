# dataportal
---
공공데이터포털 api를 이용하여 데이터를 다운로드 하기 위한 라이브러리입니다.  
xml의 경우 `OrderedDict` 형태로 데이터를 불러오고 json의 경우 `json` 형태로 데이터를 불러옵니다.
  
  
## Guide
---
```
pip install dataportal
```
사용법은 매우 간단합니다.
(예시를 위해 기상청 일기도 api를 활용하였습니다.)

아래와 같이 response부분과 데이터 다운로드 부분을 분리하여 할수도 있고

```
from dataportal import DataportalApi

url = 'http://apis.data.go.kr/1360000/WthrChartInfoService'
serviceKey = 'Test'
operation = 'getSurfaceChart'
params = {'code' : 12, 'time' : '20211118'}

dataportal = DataportalApi(url, serviceKey, operation, params)
dataportal.get_request_query()
api_out = dataportal.parse_response()
print(api_out)
```

아래와 같이 모든 과정을 한번에 처리할 수도 있습니다.
```
from dataportal import DataportalApi

url = 'http://apis.data.go.kr/1360000/WthrChartInfoService'
serviceKey = 'Test'
operation = 'getSurfaceChart'
params = {'code' : 12, 'time' : '20211118'}

dataportal = DataportalApi(url, serviceKey, operation, params)
api_out = dataportal.load(verbose=False)
print(api_out)
```
필수 파라미터가 없는 경우에 params에 아무것도 주지 않을 수 있습니다.  

```
url = 'http://api.data.go.kr/openapi'
serviceKey = 'Test'
operation = 'tn_pubr_public_cty_park_info_api'
params = {}

dataportal = DataportalApi(url, serviceKey, operation, params)
api_out = dataportal.load(verbose=False)
```

## Requires
---
* xmltodict>=0.12.0  
* requests>=2.25.1
* urllib3>=1.26.4  
