Just wanted to make something quick that gathers "good news" from numerous outlets.
Uses sentiment analysis to decide whether an article is positive or not. Sentiment analysis is NOT absolute and can very easily be wrong, so still be cautious.

In order to use:
- Clone the repo
- Navigate to https://rapidapi.com/mcdobae/api/happy-news and make an account so that you can access this specific api (Happy News) and get an API key, which you can use to replace the 'x-rapidapi-key' and 'x-rapidapi-host' variables in getNews.py
- Finally, simply run - python3 getNews.py - in your terminal and it will output the 5 top articles it got for the day, as well as output the same info to a txt file called good-news.txt.

I hope to add an automatic email feature in the future...
