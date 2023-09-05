#requests module
#! restart IDE if 3rd party module is not found after doing a proper pip install
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code) # 200 means everything is ok

print(len(res.text)) # 178978

res.raise_for_status() # if there is an error, it will raise an exception

# badRes = requests.get('https://automatetheboringstuff.com/files/fake.txt')
# badRes.raise_for_status() # raise an exception

# you need to open in binary mode to maintain unicode encoding
playFile = open('RomeoAndJuliet.txt', 'wb') # wb = write binary

for chunk in res.iter_content(100000): # 100000 bytes
    playFile.write(chunk)