#1)pip install ChatterBot chatterbot-corpus spacy
#2) python3 -m spacy download en_core_web_sm Or... choose the language you prefer
#3) Navigate to your Python3 directory
#4) Modify Lib/site-packages/chatterbot/tagging.py to properly load 'en_core_web_sm'


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer






