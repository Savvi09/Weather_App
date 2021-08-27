

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
        self.place_name = None

    def get_weather_data(self):
        self.place_name = input("Please Enter A valid City Name :")
        wurl = self.w_url.format(self.place_name)
        wreq = requests.get(url=wurl)

        if (wreq.status_code == 200):
            wdata = wreq.json()
        else :
            print('-'*20)
            print('The Entered city is in_valid')
            print('Getting the device location')
            self.place_name = self.get_user_loc()
            wurl = self.w_url.format(self.place_name)
            wreq = requests.get(url=wurl)
            wdata = wreq.json()

        return wdata

    def get_parsed_details(self):
        wdata = self.get_weather_data()

        desc = wdata['weather'][0]['description']
        temp = wdata['main']['temp']
        humidity = wdata['main']['humidity']
        wind_speed = wdata['wind']['speed']
        all_clouds = wdata['clouds']['all']

        celsius = temp - 273
        farenheit = celsius * (9 / 5) + 32

        print('-'*20)
        print("The weather details of the place - {}".format(self.place_name))
        print("Weather description - ", desc)
        print("The temp in celsius - ", round(celsius, 2))
        print("The temp in farenheit - ", round(farenheit, 2))
        print("The wind speed - {} mpg".format(wind_speed))
        print("Humidity - ", humidity)
        print("Total clouds - ", all_clouds)

        return None


ip_url = 'http://ip-api.com/json'
w_app = weatherApp(ip_url=ip_url)
w_app.get_parsed_details()


