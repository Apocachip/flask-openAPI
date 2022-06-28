import requests
from config import Config

headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Naver-Client-Id' : Config.NAVER_CLINET_ID, 'X-Naver-Client-Secret' : Config.NAVER_CLINET_SECRET}

data = {'query' : '러시아', 'display' : 30, 'sort' : 'date'}

res = requests.get(Config.NAVER_NEWS_SEARCH_URL, data, headers= headers)

res = res.json()

print(res)