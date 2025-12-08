import requests

def request_geo(road):
    apiurl = "https://api.vworld.kr/req/address?"
    params = {
        "service": "address",
        "request": "getcoord",
        "crs": "epsg:4326",
        "address": road,
        "format": "json",
        "type": "road",
        "key": '발급받은 인증키 입력'
    }

    response = requests.get(apiurl, params=params)
    json_data = response.json()
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x, y
    else:
        return 0,0

x, y = request_geo('서울특별시 성북구 안암로 145 (안암동5가, 고려대학교안암캠퍼스(인문사회계))')
print(f'x값: {x}, y값: {y}')