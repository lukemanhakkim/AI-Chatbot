from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/AIchatbotnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-xxxx', #app verification token
						   'xoxb-yyyy', # bot verification token
						   'zzzz', # slack verification token
						   True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))