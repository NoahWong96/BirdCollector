from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

class MainPage:

     def __init__(self):
         self.variable = True


    @app.route('/')
    def home():
        birdPath = "/Data/001.Black_footed_Albatross/9.jpg"
        return render_template("templates/index.html")  



if __name__ == '__main__':
    app.host(host = "0.0.0.0", port = 80)