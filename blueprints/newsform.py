from flask import Blueprint, render_template, request
from functions.webscraping import content_collector, analyze_sentiment
import os

newsformbp = Blueprint('newsform', __name__)

@newsformbp.route('/news', methods = ['POST', 'GET'])
def news():
    if request.method == 'POST':
        source = request.form['news-source']
        segment = request.form['news-segment']
        #print('HERE: ', source + segment)
        data = content_collector(source, segment)
        #print("HERE IS: ", data)
        
        results = []
        positive_count = 0
        neutral_count = 0
        negative_count = 0
        
        for sentiment in data:
            result = analyze_sentiment(sentiment)
            print(f"Text: {result['text']}")
            print(f"Sentiment: {result['sentiment']}")
            print(f"Scores: {result['scores']}\n")
            
            results.append(result)
            
            # Make sure to match the case exactly as returned by analyze_sentiment
            if result['sentiment'] == 'Positive':  # Capital P
                positive_count += 1
            elif result['sentiment'] == 'Neutral':  # Capital N
                neutral_count += 1
            elif result['sentiment'] == 'Negative':  # Capital N
                negative_count += 1
        
        return render_template('internal/newsanalysis.html', 
                              results=results, 
                              positive_count=positive_count,
                              neutral_count=neutral_count,
                              negative_count=negative_count,
                              source = source.capitalize(),
                              segment = segment.capitalize())
    
    return render_template('internal/newsform.html')