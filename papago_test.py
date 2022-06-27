# 다른 API를 이용하려면,
# requests 라이브러리를 이용하면 된다

import requests

headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Naver-Client-Id' : client_id, 'X-Naver-Client-Secret' : client_secret}

data = {'source' : 'ko', 'target' : 'en', 'text' : '만나서 반갑습니다.'}

res = requests.post(URL, data, headers= headers)

print(res.json())