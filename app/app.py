import os
from flask import jsonify, Flask, render_template, request, redirect, url_for, send_from_directory
import six.moves.urllib as urllib
import numpy as np
import requests
import urllib.request, json 
import time
import scripts.textcleaning as tc
# from scripts.plot import create_plot
import pickle
import logging
import gensim
import praw
from praw.models import MoreComments
from zipfile import ZipFile 
import flask
import pandas as pd
# from pytorch_pretrained_bert.tokenization import BertTokenizer
# from flask_cors import CORS
import datetime
import torch
# from pytorch_pretrained_bert.modeling import BertForSequenceClassification
# from helper import bert_predict

app = Flask(__name__)
# CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

label_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
max_seq_length = 256
id_to_label = {0: 'AskIndia',
 1: 'Business/Finance',
 2: 'Food',
 3: 'Non-Political',
 4: 'Photography',
 5: 'Policy/Economy',
 6: 'Politics',
 7: 'Scheduled',
 8: 'Science/Technology',
 9: 'Sports',
 10: '[R]eddiquette'}

model = pickle.load(open('model/LR.pkl','rb'))


reddit = praw.Reddit(client_id = "F4OMSR9jAi_kFQ",
					client_secret = "dBKDarfWBg7QyeZ-CXlNeLYlQ9A",
					user_agent = "web_app:reddit_scraper:v1.1.1 (by u/skadwhoosh)",
					username = "skadwhoosh",
					password = "reddit@123")

def prediction(url):
	submission = reddit.submission(url = url)
	data = {}
	data["title"] = str(submission.title)
	data["url"] = str(submission.url)
	data["body"] = str(submission.selftext)

	submission.comments.replace_more(limit=None)
	comment = ''
	count = 0
	for top_level_comment in submission.comments:
		comment = comment + ' ' + top_level_comment.body
		count+=1
		if(count > 10):
		 	break
		
	data["comment"] = str(comment)

	data['title'] = tc.clean_text(str(data['title']))
	data['body'] = tc.clean_text(str(data['body']))
	data['comment'] = tc.clean_text(str(data['comment']))
    
	combined_features = data["title"] + data["comment"] + data["body"] + data["url"]

	return model.predict([combined_features])





# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        text = flask.request.form['url']
        
        # Get the model's prediction
        flair = prediction(str(text))
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html', original_input={'url':str(text)}, result=flair,)
@app.route("/stats")
def stats():
	bar = create_plot()
	return flask.render_template('graph.html',plot=bar)


if __name__ == '__main__':
    app.run()