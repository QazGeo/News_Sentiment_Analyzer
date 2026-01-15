# Media Pulse – News Sentiment Analyzer

## Overview

**Media Pulse** is a web-based news sentiment analysis dashboard that scrapes articles from multiple news outlets, processes and stores the data in CSV format, and applies natural language processing to analyze sentiment across different news segments.

The project is built as an end-to-end pipeline; from data collection to visualization hence allowing users to explore sentiment trends through a clean, interactive dashboard rather than command-line tools.

---

## Features

* Scrape news articles from multiple online sources
* Clean and normalize raw text data
* Store processed datasets as CSV files for further analysis
* Perform sentiment analysis using VADER (NLTK)
* Interactive, product-style dashboard UI
* Sentiment breakdown into:

  * Positive
  * Neutral
  * Negative
  * Compound score
* Per-article sentiment scoring with individual visual indicators
* Aggregate sentiment summaries with visual distributions

---

## Data Storage

* All generated CSV files are stored in the **`content/`** directory
* These files can be reused for:

  * External analysis
  * Visualization
  * Model comparison
  * Historical sentiment tracking

---

## Available News Sources & Segments

### News Sources

* Currently supports **2 news outlets**
* Additional sources will be added in future updates

### Segments

* Sports
* Business
* Politics
  *(More segments planned)*

---

## How It Works

1. Select the **Try Now for Free** button
2. Select a **news source** and **segment**
3. Click **Analyze**
4. The application scrapes relevant articles (this may take a few seconds)
5. You are redirected to a results page that displays:

   * Total article count
   * Sentiment distribution (positive, neutral, negative)
   * Aggregate sentiment summaries with visual indicators
   * Individual article sentiment scores
   * Compound sentiment visualization per article

Each record includes:

* The original cleaned text
* Individual sentiment scores
* A compound score
* A small visual representation of sentiment strength

---

## Tech Stack

**Frontend**

* HTML
* Tailwind CSS

**Backend**

* Python
* Flask

**Data Processing**

* Pandas

**Natural Language Processing**

* NLTK (VADER Sentiment Analyzer)

**Web Scraping**

* BeautifulSoup

---

## Installation & Usage

There is no complex installation process.

1. Clone or download the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:

   ```bash
   python app.py
   ```
4. Open your browser and navigate to:

   ```
   http://localhost:5000
   ```

---

## Use Cases

* Analyzing general sentiment within a specific market or sector
* Enabling data-driven decision-making before major trades
* Investigative or analytical research in business and politics
* Understanding media tone and narrative trends across outlets

**Example:**
Evaluating sentiment in the *business* or *politics* segment before making a high-risk investment decision.

---

## Challenges Faced

One of the main challenges in this project was transitioning from **Bootstrap to Tailwind CSS**.

Coming from a Bootstrap background, implementing Tailwind required:

* Moving away from predefined components
* Relying heavily on documentation
* Learning utility-based styling patterns
* Using tutorials to understand class naming and layout control

Although challenging, this shift helped improve flexibility in UI design and strengthened overall CSS understanding.

---

## Limitations

* **BeautifulSoup only supports HTML-based scraping**

* JavaScript-rendered pages are not supported
* Scraping speed depends on the source and article volume
* Limited number of news sources and segments at present

---

## Future Improvements

* Add more news sources
* Expand available segments
* Improve dashboard interactivity
* Add scheduled scraping
* Optional database integration for faster querying

---

## License

Copyright © 2026 George Rading. All rights reserved.

This repository is publicly accessible for viewing purposes only.
No permission is granted to copy, modify, distribute, or use this code,
in whole or in part, for any purpose without explicit written consent
from the author.

---
