from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import tkinter as tk


def pregunta():
    pre = preg.get()
    chat = chatBot.get_response(pre)
    return var.set(chat)

ventana = tk.Tk()

ventana.title("MathBot")
# ancho por alto
ventana.geometry('360x250')
ventana.configure(background='light grey')

#chatbot

chatBot = ChatBot('MathBot')
entrenar = ChatterBotCorpusTrainer(chatBot)
entrenar.train('chatterbot.corpus.spanish')

while True:
    # variables
    var = tk.StringVar()
    res = tk.StringVar()

    preg = tk.Entry(ventana)
    preg.place(x=10, y=200, relwidth=0.7, relheight=0.1)

    btn = tk.Button(ventana, text="Enviar", command=pregunta, cursor="hand2", bg="sky blue", width=10, relief="flat")
    btn.place(x=270, y=200)

    re = tk.Label(ventana, bg="blue", textvariable=var, padx=5, pady=5, width=50)
    re.pack()

    ventana.mainloop()

