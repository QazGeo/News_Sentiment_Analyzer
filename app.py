from flask import render_template, Flask


from blueprints.newsform import newsformbp

app = Flask(__name__)

app.register_blueprint(newsformbp)

@app.route('/')
def home():
    return render_template("internal/index.html")



app.run(debug = True)