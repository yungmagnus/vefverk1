from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    #the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <a href="sida2">Síða 2</a>
    <a href="sida3">Http Spurningar</a>

    <img src="http://loremflickr.com/600/400">
    """#.format(time=the_time)

@app.route('/sida2')
def page2():
    #the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return """
    <h1>Sup dude</h1>
    <p>It is currently {time}.</p>
    <a href="/">Forsíða</a>
    <a href="sida3">Http Spurningar</a>

    <img src="http://loremflickr.com/600/400">
    """#.format(time=the_time)
@app.route('/sida3')
def page3():
    #the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return render_template("sida3.html")
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)