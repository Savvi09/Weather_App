
import requests

class DeviceTracker:
    def __init__(self,url):
        self.url = url

    def get_device_data(self):
        req_data = requests.get(url=self.url)
        if (req_data.status_code == 200):
            req_json = req_data.json()

        else :
            req_json = None

        return req_json

    def get_user_loc(self):
        req_json = self.get_device_data()
        if req_json:
            city_name = req_json['city']
        else:
            city_name = None

        return city_name

url = 'http://ip-api.com/json'
ip_dev = DeviceTracker(url=url)
print(ip_dev.get_user_loc())
