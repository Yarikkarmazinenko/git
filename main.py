import json
import csv

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/hello")
def hello():
    return render_template("hello.html")


@app.route("/goodbye")
def goodbye():
    # text_1 = text.upper()
    return render_template("goodbye.html")


@app.route("/brand")
def brand():
    return render_template("brand.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact_show",methods=["POST"])
def contact_show():
    name=request.form["name"]
    text=request.form["text"]
    info={
        "name": name,
        "text": text,
    }
    print(info)
    with open("database/info.json","a") as file:
        json.dump(info,file)
    with open("database/file.csv", "a+") as f:
        for k,v in info.items():
            s = f"{k},{v}\n"
            f.write(s)
        # f.write(info["name"])
        # f.write(info["text"])
        f.seek(0)
        reader = csv.reader(f)
        show_list = []
        for row in reader:
            show = ",".join(row)
            show_list.append(show)
            print(show)

    return render_template("contact_show.html",name=name, text=text,show=show_list)


@app.route("/dog/<dog_name>/<int:year>")
def dog(dog_name,year):
    print(dog_name,year)
    return render_template("dog.html", my_dog = dog_name,dog_year = year)

@app.route("/tiger/<int:tiger>")
def tiger(tiger):
    print(tiger)
    return render_template("index.html", tiger = tiger)

@app.route("/cat/<int:cat>")
def cat(cat):
    print(cat)
    return render_template("cat.html", cat=cat)

if __name__ == '__main__':
    app.run(debug=True)
