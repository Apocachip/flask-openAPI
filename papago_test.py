# 다른 API를 이용하려면,
# requests 라이브러리를 이용하면 된다

import requests
from config import Config

headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Naver-Client-Id' : Config.NAVER_CLINET_ID, 'X-Naver-Client-Secret' : Config.NAVER_CLINET_SECRET}

data = {'source' : 'ko', 'target' : 'en', 'text' : '만나서 반갑습니다.'}

res = requests.post(Config.NAVER_PAPAGO_URL, data, headers= headers)

print(res.json())