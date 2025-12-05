import requests
import re

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[0]
print(out_addr)
