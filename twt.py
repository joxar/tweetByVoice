# encoding: utf-8
import requests

TOKEN = ""
URL = "https://maker.ifttt.com/trigger/voiceTweet/with/key/"

requests.post(URL + TOKEN, json = {'value1':'ためしにツイート'})

