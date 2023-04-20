import re
import details
import random
import tkinter as tk
import sys
import time

# when the highest probability of any response will not be greater than 1
# means it will not be matching with any list of words that are stored then this function will be called 
# signifying that data is not present   
def unknown():
    response = ["Could you please re-phrase that? ",
                "I'm sorry, I didn't quite catch that. \n     Could you please repeat it?",
                "What does that mean?",
                "Sorry for inconvinience but i was not able to \n     understand what do you want to say"][
        random.randrange(4)]
    return response

# calculates the probability of the particular response according to user input
def msg_prob(user_inp , recognised_words , single_resp = False , required_words = []):
    msg_certainity = 0
    has_required_words = True

    # if the word in user written text is present in recognised_words then increasing message certainity 
    # means it's more accurate sentence
    for word in user_inp: 
        if word in recognised_words:
            msg_certainity += 1

    percentage = float(msg_certainity) / float(len(recognised_words))

    # checking for certain words that should be there in this senctence and if not present then change the flag for required words 
    for word in required_words:
        if word not in user_inp:
                has_required_words = False
                break

    # returns the probability
    if required_words or single_resp:
        return int(percentage * 100)
    else: 
        return 0

# returns the response of the bot
def chk_msg(user_msg):
    highest_prob_list = {}

    # updates the highest probability list which contains the probability of all the responses stored 
    def response(bot_resp , list_of_words , single_response = False , required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_resp] = msg_prob(user_msg , list_of_words , single_response , required_words)
    
    # Responses
    response('Hello! How can I help you ?', ['hello', 'hi', 'hey', 'sup', 'hola' , 'helo'], single_response = True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how','you'])
    response('You\'re welcome! If you need any more assistance in     the future, feel free to ask. I\'m here to help!', ['thank', 'thanks'], single_response = True)
    response(f"Sure , Your current balance is {p1.chk_balance()} Rs",['can' , 'check' , 'my' ,'balance'] , required_words = ['my' , 'balance'] )
    response(f"Account status = {p1.acc_stat()},\n      Account activation = {p1.acc_act()},\n      Account type = {p1.acc_type()}\n      To know more you can contact us on Toll free number :- 1800-564-9548" ,[ 'some','provide','details', 'information' , 'my' , 'account'] , required_words=['details' , 'information'])
    response(f"Account status = {p1.acc_stat()}" , ['what' , 'status' , 'account'] , required_words=['status' , 'account'])
    response(f"Account activation date = {p1.acc_act()}" , ['what','is','activation' , 'date','acocount'] , required_words=['activation' , 'what'])
    response(f"Please check this out on our web \n     https://abcbank.com" , ['can','you','about','loans','your','bank','provide'] , required_words=['loans'])
    response(f"You can contact us on Toll free number \n     :- 1800-564-9548" , ['can','provide','me','your','customer care'] , required_words=['customer care'])
    response(f"You can call us anytime on :- 1800-564-9548" , ['how' , 'connect','contact', 'with','your', 'customer care'] , required_words = ['customer care'])

    best_match = max(highest_prob_list , key = highest_prob_list.get)
    # print(highest_prob_list)

    # returning best response according to probability
    return unknown() if highest_prob_list[best_match] < 1 else best_match
    

# removes the characters except alphabets and passes the user input as a list
def bot_responses(user):
    user_msg = re.split(r'\s+|[,;?!.-]\s*', user.lower())
    response = chk_msg(user_msg)
    return response

def login_window():
    screen = tk.Tk()
    screen.title("login")
    screen.geometry("450x300")
    screen.resizable(False,False)
    screen.configure(bg = "white")
    name = tk.StringVar()
    id = tk.StringVar()
    global passw
    passw = tk.StringVar()

    tk.Label(screen,text="Login here",font="Times 20",fg="black",bg = "white").pack(fill="both")
    tk.Label(screen , text="Name" , font="20",bg = "white").place(x = 45 , y = 50)
    tk.Label(screen,text="Id",font="20",bg = "white").place(x=45,y=100) 
    tk.Label(screen,text="Password",font="20",bg = "white").place(x=45,y=150)

    name_loginenter = tk.Entry(screen , font="10",bd="4",textvariable = name)
    name_loginenter.place(x=205 , y = 50)

    regno_loginenter=tk.Entry(screen,font="10",bd="4",textvariable = id)
    regno_loginenter.place(x=205,y=100)

    pass_loginenter=tk.Entry(screen,font="10",bd="4",textvariable = passw)
    pass_loginenter.place(x=205,y=150)


    def login():
        global p1
        p1 = details.Acc_Detail(name.get() , id.get())
        if p1.validate_login(passw.get()) == False:
            # tk.Label(screen , text = "Unable to login , please check your password!!",font = "Times 15",fg="red",bg = "white").place(x = 45,y = 210)
            print("Unable to login")
            sys.exit(0)
        # else :
            # tk.Label(screen , text = "Successful Login",font = "Times 15",fg="green",bg = "white").place(x = 55,y = 210)
        screen.destroy()
        

    
    tk.Button(screen, text="Login",font="50",bg="blue",fg="white",command=login).place(x=185,y=250)
    screen.mainloop()


    

def chatbot_response():
    message = entry.get()
    response = bot_responses(message)
    text.insert(tk.END, f"{p1.name}: " + message + "\n")
    text.insert(tk.END, "Bot: " + response + "\n\n")
    entry.delete(0, tk.END)

login_window()

root = tk.Tk()
root.title("Chatbot")

frame = tk.Frame(root)

tk.Label(root,text = "ABC Bank",font="Times 20",fg="black").pack(fill="both")
scrollbar = tk.Scrollbar(frame)

text = tk.Text(frame, height = 25, width = 55, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.pack(side=tk.LEFT, fill=tk.BOTH)
frame.pack()
text.insert(tk.END,f"Bot: Hello! How can I help you {p1.name}?\n\n")

entry = tk.Entry(root, width = 60)
entry.pack(side = tk.LEFT, padx=10, pady=10)

button = tk.Button(root, text="Send",bg="green",fg="white" ,command = chatbot_response)
button.pack(side = tk.LEFT, padx=10, pady=10)

root.mainloop()
