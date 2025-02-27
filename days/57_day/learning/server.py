import datetime

from flask import Flask, render_template
from random import randint
from datetime import datetime as dt
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    random_number = randint(1,10)
    time = datetime.datetime.now()
    current_year = time.strftime("%Y")
    return render_template("index.html",num=random_number, current_year=current_year)

@app.route("/guess/<name>")
def find_name(name):
    agify_url = f"https://api.agify.io?name={name}"
    genderize_url= f"https://api.genderize.io?name={name}"

    age_response = requests.get(url=agify_url)
    age_response.raise_for_status()
    print(age_response.json())
    age = age_response.json()['age']
    gender_response = requests.get(url=genderize_url)
    gender=gender_response.json()['gender']
    return render_template("guess.html",name=name,gender=gender,age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html",posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)