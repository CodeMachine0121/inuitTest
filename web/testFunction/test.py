import requests

res =requests.get('www.google.com').text
print(res)