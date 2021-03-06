from flask import render_template, url_for, redirect, request
from analyzer import app
from analyzer.twitter_funcs import *


@app.route("/", methods=['GET', 'POST'])
def home():
	tweets = get_tweets()
	tweets_count = get_recent_tweets_count(tweets)
	tweets_good, good_tweets_count, bad_tweets_count = get_tweet_sentiment(tweets)

	if tweets_good == True:
		text_type = "text-success"
	else:
		text_type = "text-danger"

	return render_template('home.html', tweets_count=tweets_count, text_type=text_type, good_count=good_tweets_count, bad_count=bad_tweets_count)


@app.route("/tweets")
def tweets():
	tweets = get_tweets()
	return render_template('tweets.html', tweets=tweets)


@app.route("/tweets/<technical_or_not>")
def toggle_tweets(technical_or_not):
	if technical_or_not == "technical":
		is_technical = True
	elif technical_or_not == "not-technical":
		is_technical = False

	tweets = get_tweets(is_technical)

	return render_template('tweets.html', tweets=tweets)


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if email == 'admin@admin.com' and password == 'admin':
			return redirect(url_for('home'))

	return render_template('login.html')