from flask import Blueprint, render_template, request

newsformbp = Blueprint('newsform', __name__)

@newsformbp.route('/news', methods = ['POST', 'GET'])
def news():
    if request.method == 'POST':
        source = request.form['news-source']
        segment = request.form['news-segment']
        print('HERE: ', source + segment)
    return render_template('internal/newsform.html')