import requests

URL = 'https://search.naver.com/search.naver'
params = {'query':'aa'}
response = requests.get(URL, params=params)
print(response.status_code)
print(response.text)