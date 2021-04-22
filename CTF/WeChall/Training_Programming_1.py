import requests


cookies = {'WC': "13184222-55406-Z4AoDr5EB3FGg2s6"}
url = 'https://www.wechall.net/challenge/training/programming1/index.php'
param = {'action': 'request'}
r = requests.get(url, params=param, cookies=cookies)


param = {'answer': r.text}
r = requests.post(url, cookies=r.cookies, params=param)
