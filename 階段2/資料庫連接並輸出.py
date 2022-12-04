import urllib.request as request
import json 
import flask 
url="https://api.jsonstorage.net/v1/json/5f186bb3-4ab3-4dfe-91d8-62e18bcc9dcf/2f766411-2f74-4ea3-a161-053a8867e1e7"
with request.urlopen(url) as getdata:
    data=json.load(getdata)

out=data['text']#取得資料庫中的text的
print(out)
