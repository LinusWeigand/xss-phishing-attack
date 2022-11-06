import requests

if __name__ == '__main__':
    session = requests.Session()
    # Make a post request
    page = session.post('http://172.25.52.49:43579', data={'address' : 'this is the html bodyyy!!'})
    print(page.text)