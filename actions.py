from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import requests
import json
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset, Restarted

class ActionWeather(Action):
	"""
	To get the weather details
	"""
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):

		api_key = 'xxxxNeed news api key herexxxx'
		loc = tracker.get_slot('location')
		url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(loc, api_key)
		r = requests.get(url)
		api_response = r.json()
		city = api_response['name']
		condition = api_response['weather'][0]['description']
		temperature_c = api_response['main']['temp']
		humidity = api_response['main']['humidity']
		wind_mph = api_response['wind']['speed']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)

		dispatcher.utter_message(response)
		return [SlotSet('location', None)]

class ActionNews(Action):
	"""
	To get the specific news
	"""
	def name(self):
		return 'action_news'

	def run(self, dispatcher, tracker, domain):
		news = tracker.get_slot('newstories')
		#print("the newstories is :", news)
		#return news
		url = ('https://newsapi.org/v2/everything?'
			   'q={}&'
			   'from=2019-11-04&'
			   'sortBy=popularity&'
			   'apiKey=xxxxNeed news api key here'.format(news))

		response = requests.get(url)
		r = response.json()
		news_list = r['articles']
		news_count=0
		for news in news_list:
			news_count+=1
			if news_count==10:
				break
			title = news['title']
			description = news['description']
			url = news['url']
			print("\n")
			response = """{0},
						  {1},
						  {2}""".format(title, description, url)
			dispatcher.utter_message(response)
		return [SlotSet('newstories', None)]

#To reset the slot
class ResetSlot(Action):
    def name(self):
        return "action_reset_slot"
    def run(self, dispatcher, tracker, domain):
        return [SlotSet('location', None)]