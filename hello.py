import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='127.0.0.1', threaded=True)

url = "https://greatday.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
quote_from_greatday = soup.find(id="theQuote")
print(type(quote_from_greatday))
print("convert bs4.element.tag object to str object")
quote_string = quote_from_greatday.text
print(type(quote_string))
print("Quote from greatday.com received")
print("-----------")
print(quote_from_greatday)
print("-----------")

@app.route("/data", methods=['POST', 'GET'])
def data():
    return render_template("form.html", quote=quote_string)

@app.route("/", methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return render_template("hello.html", quote_of_the_now="hi")
    if request.method == 'POST':
        # form_data_from_submit = request.form
        # return render_template("quote_from_greatday.html", form_data = form_data_from_submit)
        # print(form_data_from_submit)
        return "something off"

