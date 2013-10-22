#!/usr/bin/env python
# Utility sctipt to automatically submit credentials to INSA LYON wireless captive portal 
# Place in /etc/NetworkManager/dispatcher.d for seamless operation

import NetworkManager,requests

USERNAME = ""
PASSWORD = "CHANGEME"

for conn in NetworkManager.NetworkManager.ActiveConnections:
    settings = conn.Connection.GetSettings()   
ssid = settings['802-11-wireless']['ssid']
if('INSA-INVITE'==ssid):
    payload = {'user': USERNAME,'password':PASSWORD,'cmd':'authenticate','fqdn':'insa-lyon.fr','Login':'Log+In'}
    url='https://securelogin.arubanetworks.com/cgi-bin/login'
    r= requests.post(url, data=payload,verify=False)   

