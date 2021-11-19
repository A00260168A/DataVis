import tweepy
from flask import Flask, render_template, request
import os
import tweepy as tp
import pandas as pd
import json

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['CSV_FOLDER'] = 'static/CSV'

consumer_key = '7QYQH7qf0q9Lk3XNChkoJpWtQ'
consumer_secret = '8URqQMLRulnBZ2zBg6INwgBcSy1n2nmqcivQrLevgOXLBuVoLd'
access_token = '1440589430016729096-4foIMmmDWo3HlPX4F118EgV3MP43bL'
access_token_secret = 'nCdz73VOiNPH1V4QVZsnwvRdlOMxAFahvUMQWSuqdNcC0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


query = "west ham"


@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        print("here")
        tweets = tp.Cursor(api.search_tweets, q=query, lang="en", result_type="popular").items(20)

        for tweet in tweets:
            print(tweet.text)

    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)
