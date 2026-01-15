import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime, timezone


def content_collector(source, segment):
    data = []

    url = f'https://{source}/{segment}'

    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, 'html.parser')
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        text = paragraph.get_text()
        if len(text.split()) > 5:
            data.append()


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    csv_file = f'/content/{source}_{segment}_{timestamp}.csv'

    df = pd.DataFrame(data, columns=['NewsContent'])
    
    csv_file = f'/content/{source}_{segment}_{timestamp}.csv'
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')
    
    return df
