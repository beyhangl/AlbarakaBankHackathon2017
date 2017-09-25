from chatterbot import ChatBot




def trainet():
 chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
 )

 # Train based on the english corpus
 chatbot.train("chatterbot.corpus.english")

 # Get a response to an input statement
 return chatbot
def sonuc_getir(gelen_text):
 print(chatbot.get_response(str(gelen_text)))

~
~
