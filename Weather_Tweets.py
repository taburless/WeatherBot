#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Dependencies
import tweepy
import time
import json
import random
from pprint import pprint
import requests as req
import datetime
import os
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
weather_api_key = os.environ.get("weather_api_key")

# In[15]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[16]:


# Weather API Key
api_key = weather_api_key


# In[27]:


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    dc_weather = weather_json['main']['temp']
    pprint(dc_weather)
    
    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(f"Now the weather is DC is {dc_weather}. Not a bot")


    # Print success message
    print(f"Iteration #, {dc_weather}")


# In[28]:


# Set timer to run every 1 hour
while(True):

    # Call the WeatherTweet function and specify the tweet number
    WeatherTweet()

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(3600)


# In[ ]:




