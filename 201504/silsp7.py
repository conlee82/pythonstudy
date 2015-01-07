import requests

r = requests.get('http://c1.img.netmarble.kr/web/netmarble/main/v/img/logo.gif')
#print (r.content)

with open('netmarble-logo.gif', 'wb') as file:
    for chunk in r.iter_content():
        file.write(chunk)