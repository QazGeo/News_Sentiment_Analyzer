from flask import Blueprint, render_template, request
from functions.webscraping import content_collector

newsformbp = Blueprint('newsform', __name__)

@newsformbp.route('/news', methods = ['POST', 'GET'])
def news():
    if request.method == 'POST':
        source = request.form['news-source']
        segment = request.form['news-segment']
        print('HERE: ', source + segment)
        content_collector(source, segment)
    return render_template('internal/newsform.html')