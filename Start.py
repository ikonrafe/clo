import requests
import pygame
import googlemaps

api_key = 'AIzaSyAuUqm6atdaFjkBmo3k9pge86qH31am1FU'
phone_number = input("Masukkan nomor telepon yang ingin dilacak: ")

def show_matrix(screen):
    font = pygame.font.SysFont('Consolas', 20)
    text = font.render("iclone_Rfe", True, (0, 255, 0))
    screen.blit(text, (0, 0))
    for i in range(40):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((0, 0, 0))
        font_name = pygame.font.SysFont('Consolas', 30)
text_name = font_name.render("iclone_RFE", True, (255, 0, 0))
screen.blit(text_name, (20, 20))

        for j in range(i):
    text = font.render("010101010101010101010101010101010101010101010101010101010101010101", True, (0, 255, 0))
    screen.blit(text, (0, j*12))
pygame.display.flip()
pygame.time.wait(50)

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

def main():
    pygame.init()
    pygame.display.set_caption("Matrix")
    screen = pygame.display.set_mode((600, 400))
    show_matrix(screen)
    locate_phone(api_key, phone_number)
    pygame.quit()

if __name__ == "__main__":
    main()

#install dulu(pip install -U googlemaps) sebelum di jalankan
