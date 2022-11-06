from flask import Flask, request, abort
import requests


# create a flask server
# it can handle a post request with the parameter 'name'
# if it receives a post request, it will print out the whole response

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        print("NAME: " + name)
        return "ok"


if __name__ == '__main__':
    # session = requests.Session()
    # Make a post request
    # page = session.post(url, data={'contacttext': f'{xss_url}'})
    app.run()


    