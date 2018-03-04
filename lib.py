import requests

def new_ip():
    n = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=e99d8488223f1a43f9ba34e89e598ae4&sep=3')
    return n.text.strip()
