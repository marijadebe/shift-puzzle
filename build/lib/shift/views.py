from shift import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/game/<int:size>')
def game(size: int = 4):
    if 3 <= size <= 7: return render_template("game.html", size=size)
    else: return render_template("error.html", type=403), 403
    
@app.errorhandler(404)
def pageNotFound(error):
    return render_template("error.html", type=404), 404
