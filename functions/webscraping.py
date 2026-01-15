import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def content_collector(source, segment):
    data = []

    url = f'https://{source}.com/{segment}'

    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, 'html.parser')
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        text = paragraph.get_text()
        if len(text.split()) > 5:
            data.append(text)


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    csv_file = f'content/{source}_{segment}_{timestamp}.csv'

    df = pd.DataFrame(data, columns=['NewsContent'])
    
    csv_file = f'content/{source}_{segment}_{timestamp}.csv'
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')

    return data


def analyze_sentiment(text):
    """
    Analyze sentiment of input text using VADER model
    Returns polarity scores and overall sentiment label
    """
    # Initialize the VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()
    
    # Get polarity scores
    scores = sia.polarity_scores(text)
    
    # Determine overall sentiment based on compound score
    if scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif scores['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return {
        'text': text,
        'scores': scores,
        'sentiment': sentiment
    }