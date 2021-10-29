from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatBot = ChatBot('MathBot')


entrenar = ChatterBotCorpusTrainer(chatBot)
entrenar.train('chatterbot.corpus.spanish')


while True:
    pregunta = input('Yo: ')
    respuesta = chatBot.get_response(pregunta)
    print('MathBot: ', respuesta)