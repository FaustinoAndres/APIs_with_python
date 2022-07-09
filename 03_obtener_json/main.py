from urllib import response
import requests
import json

if __name__ == '__main__':

    url = 'http://httpbin.org/get'
    args = { 'nombre': 'Faustino' }

    response = requests.get(url, params=args)

    if response.status_code == 200:

        response_json_2 = response.json()
        origin = response_json_2['origin']
        print(origin)

        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)
