

import requests



class DeviceTracker:
    def __init__(self,ip_url):
        self.ip_url = ip_url

    def get_device_data(self):
        ip_req = requests.get(url=self.ip_url)
        ip_data = ip_req.json()
        return ip_data

    def get_user_loc(self):
        ip_data = self.get_device_data()
        city_name = ip_data['city']
        return city_name



class weatherApp(DeviceTracker):
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
            place_name = self.get_user_loc()
            wurl = self.w_url.format(place_name)
            wreq = requests.get(url=wurl)
            wdata = wreq.json()

        return wdata

ip_url = 'http://ip-api.com/json'
w_app = weatherApp(ip_url=ip_url)
print(w_app.get_weather_data())


