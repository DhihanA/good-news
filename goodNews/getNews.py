import os
from dotenv import load_dotenv
load_dotenv()
import http.client
import json
# import re
# import smtplib
# https://pypi.org/project/email-validator/
# from email_validator import validate_email, EmailNotValidError


# https://rapidapi.com/mcdobae/api/happy-news/playground/apiendpoint_f3998bdc-01b0-4fe5-bd84-033a55e9a19c
conn = http.client.HTTPSConnection("happy-news.p.rapidapi.com")
headers = {
    'x-rapidapi-key': os.getenv('X-RAPIDAPI-KEY'),
    'x-rapidapi-host': os.getenv('X-RAPIDAPI-HOST')
}

# all possible endpoints for this API
channels = ['/bbc', '/cnn', '/aljazeera', '/sky', '/dailymail', '/theguardian', '/independent']
articles = []

# testing it out with just 1 channel atm
conn.request("GET", '/cnn', headers=headers) # making the req with the channel right now
res = conn.getresponse() 
raw_data = res.read() # this is just raw byte data
decoded_data = raw_data.decode("utf-8") # the decoded byte data (converts it into a str)
parsed_data = json.loads(decoded_data) # goes ahead and actually parses the prev decoded byte data str into its respective data type (in this case, a list of dicts)
articles.extend(parsed_data) 

# # getting articles from all 7 possible channels
# for ch in channels:
#     conn.request("GET", ch, headers=headers) # making the req with the channel right now
#     res = conn.getresponse() 
#     raw_data = res.read()
#     decoded_data = raw_data.decode("utf-8")
#     parsed_data = json.loads(decoded_data)
#     if parsed_data: articles.extend(parsed_data)


# https://stackoverflow.com/questions/9427163/remove-duplicate-dict-in-list-in-python
# for some reason the api returns duplicate articles, so im removing duplicate dicts from the list
articles = [dict(tup) for tup in {tuple(di.items()) for di in articles}]
print(articles)
articles.sort(key=lambda obj: obj['score'], reverse=True)

# only getting first 5 articles?
if len(articles) > 5: articles = articles[:5]

print('-------')
print(articles) # seeing if it's actually sorted

# just making sure of something
# test_articles = [{'title': 'Example 1', 'url': 'https://wikipedia.com', 'score': 10}, {'title': 'suck eggs', 'url': 'https://nintendo.com', 'score': 100}]
# print()
# for obj in test_articles:
#     print(obj['title'])
#     print(obj['url'])
    # print()

# printing out the articles to the terminal
index = 1
print()
for obj in articles:
    print(f"{index}. {obj['title']}")
    print(f"   {obj['url']}")
    print()
    index += 1

# https://stackoverflow.com/questions/899103/writing-a-list-to-a-file-with-python-with-newlines
# as well as writing the articles to a txt file for them to see
index = 1
with open('good-news.txt', 'w') as f:
    for obj in articles:
        f.write(f"{index}. {obj['title']}\n")
        f.write(f"   {obj['url']}\n")
        f.write("\n")
        index += 1


# future emailing feature
# def validate_email(email):
#     pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
#     return re.match(pattern, email)

# user_email = input("Please enter your email address to get your good news: ")

# if not validate_email(user_email): 
#     print("Invalid email. Please try again.")
#     exit(1)

# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# s.login("email-goes-here", "password-goes-here")
# message = "Message_you_need_to_send"
# s.sendmail("email-goes-here", user_email, message)
# s.quit()