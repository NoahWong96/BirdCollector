from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


class Application:

    def __init__(self):
        self.variable = True

    @app.route('/botd')
    def home():
        birdName = "Black Footed Albatross"
        return render_template("BOTD.html", value=birdName)

    @app.route('/random')
    def showRandomBird():
        return render_template("RandomBird.html")

    @app.route('/<int:birdnumber>')
    def showSpecificBird(birdnumber):
        return render_template("specificbird.html", birdnumber=birdnumber)

    @app.route('/admin')
    def admin():
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
