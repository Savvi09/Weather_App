

import requests

class weatherApp:
    def __init__(self,ip_url):
        self.ip_url  = ip_url
        self.w_url ='https://api.openweathermap.org/data/2.5/weather?q={}&appid=9d41bd4e5bffd04e03a6cb6832066559'

    def get_weather_data(self):
        place_name = input("Please Enter A valid City Name :")
        wurl = self.w_url.format(place_name)
        wreq = requests.get(url=wurl)

        if (wreq.status_code == 200):
            wdata = wreq.json()
        else :
            wdata = {}

        return wdata

url = 'http://ip-api.com/json'
w_app = weatherApp(ip_url=url)
print(w_app.get_weather_data())


