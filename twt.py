import requests

TOKEN = ""
URL = "https://maker.ifttt.com/trigger/voiceTweet/with/key/"

requests.post(URL + TOKEN, json = {'value1':'abc'})

