#requests module
#! restart IDE if 3rd party module is not found after doing a proper pip install
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code) # 200 means everything is ok