from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

engine=pp.init()

    
#install : pip install chatterbot
#install :pip install pyttsx3



bot = ChatBot("MY CHATBOT")
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
    "Where do you Live?",
    "I am an AI i cant defined this"
    "OK"
    "Can i help you?"
]

trainer = ListTrainer(bot)

trainer.train(conversation)

main = Tk()
main.geometry("500x650")
main.title("My CHATBOT")
img = PhotoImage(file="chat.png")

#photoL = Label(main,image=img)
#photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"you : " + query)       
    msgs.insert(END,"bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame , width=80, height=20,yscrollcommand=sc.set)

sc.pack(side=RIGHT , fill=Y)
msgs.pack(side=LEFT, fill=BOTH , pady =10)
frame.pack()


#creating textfield
textF = Entry(main,font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main,text="Ask from bot", font=("Verdana",20),command=ask_from_bot)
btn.pack()

#creating a fnction
def enter_function(event):
    btn.invoke()


#going to bind main window with enter key
main.bind('<Return>', enter_function)


main.mainloop()
