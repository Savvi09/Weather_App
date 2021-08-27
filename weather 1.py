

import requests

class DeviceTracker:

    def __init__(self,ip_url):
        self.ip_url = ip_url

    def get_device_data(self):
       req_data = requests.get(url=self.ip_url)
       if(req_data.status_code == 200):
           req_json =req_data.json()
       else:
           req_json = {}
       return req_json

url = "http://ip-api.com/json"
ip_dev = DeviceTracker(ip_url=url)
print(ip_dev.get_device_data())

