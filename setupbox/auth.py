import requests

resp = requests.get('http://fast0.ajou.ac.kr:8080/authTest', auth=('maxtortime@gmail.com', '123456'))

print(resp.text)