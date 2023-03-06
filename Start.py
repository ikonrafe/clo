import requests

import googlemaps

api_key = 'YOUR_API_KEY'

phone_number = '6281236022306'

def locate_phone(api_key, phone_number):

    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key={}'.format(api_key)

    headers = {'content-type': 'application/json'}

    data = {

        'considerIp': 'false',

        'wifiAccessPoints': [],

        'cellTowers': [{

            'cellId': 35148066,

            'locationAreaCode': 36,

            'mobileCountryCode': 510,

            'mobileNetworkCode': 10

        }]

    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:

        location = response.json()['location']

        accuracy = response.json()['accuracy']

        print(f'Phone {phone_number} is at ({location["lat"]}, {location["lng"]}), accuracy: {accuracy} meters')

        # Reverse geocoding to get the address

        gmaps = googlemaps.Client(api_key)

        reverse_geocode_result = gmaps.reverse_geocode((location["lat"], location["lng"]))

        address = reverse_geocode_result[0]['formatted_address']

        print('Address:', address)

    else:

        print('Unable to locate phone')

locate_phone(api_key, phone_number)

# install dulu (pip install -U googlemaps"
