import os
import requests
from countries import dict as countries


codes = countries.keys()
success_count = 0
print(f'Flags count: {len(codes)}')
print('Downloading flags:')
if os.path.isdir('flags'):
    print('"flags" directory already exists!')
    exit()
os.mkdir('flags')
if not os.path.isdir('flags'):
    print('"flags" directory has not been created!')
    exit()
try:
    for code in codes:
        url = f'https://www.worldatlas.com/r/w425/img/flag/{code.lower()}-flag.jpg'
        r = requests.get(url)
        with open(f'flags/{code}.jpg', 'wb') as f:
            f.write(r.content)
            print(f'Successully downloaded: {code} flag')
            success_count += 1
except KeyboardInterrupt:
    pass
print(f'Success: {success_count}')
