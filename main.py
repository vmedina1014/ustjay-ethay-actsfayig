import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    response=requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText()


@app.route('/')
def home():
    fact=get_fact()
    url="https://hidden-journey-62459.herokuapp.com/piglatinize/"
    data={'input_text':fact}
    response=requests.post(url, data=data, allow_redirects=False)
    new_url=response.headers['Location']
    return "<a href='{}'>{}</a>".format(new_url,new_url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)