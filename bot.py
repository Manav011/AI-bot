import re
import details
import random

# when the highest probability of any response will not be greater than 1
# means it will not be matching with any list of words that are stored then this function will be called 
# signifying that data is not present   
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "What does that mean?",
                "Sorry for inconvinience but i was not able to understand \n      what do you want to say"][
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
    response('Hello!\n      How can I help you ?', ['hello', 'hi', 'hey', 'sup', 'hola' , 'helo'], single_response = True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how','you'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response = True)
    response(f"Sure , Your current balance is {p1.chk_balance()} Rs",['can' , 'check' , 'my' ,'balance'] , required_words = ['my' , 'balance'] )
    response(f"Account status = {p1.acc_stat()},\n      Account activation = {p1.acc_act()},\n      Account type = {p1.acc_type()}\n      To know more you can contact us on Toll free number :- 1800-564-9548" ,[ 'some','provide','details', 'information' , 'my' , 'account'] , required_words=['details' , 'information'])
    response(f"Account status = {p1.acc_stat()}" , ['what' , 'status' , 'account'] , required_words=['status' , 'account'])
    response(f"Account activation date = {p1.acc_act()}" , ['what','is','activation' , 'date','acocount'] , required_words=['activation' , 'what'])
    response(f"Please check this out on our web https://abcbank.com" , ['can','you','about','loans','your','bank','provide'] , required_words=['loans'])
    response(f"You can contact us on Toll free number :- 1800-564-9548" , ['can','provide','me','your','customer care'] , required_words=['customer care'])
    response(f"You can call us anytime on :- 1800-564-9548" , ['how' , 'connect','contact', 'with','your', 'customer care'] , required_words = ['customer care'])

    best_match = max(highest_prob_list , key = highest_prob_list.get)
    print(highest_prob_list)

    # returning best response according to probability
    return unknown() if highest_prob_list[best_match] < 1 else best_match


# removes the characters except alphabets and passes the user input as a list
def bot_responses(user):
    user_msg = re.split(r'\s+|[,;?!.-]\s*', user.lower())
    response = chk_msg(user_msg)
    return response



name , id = input("Enter your name and user id: ").split()
p1 = details.Acc_Detail(name , id)
passw = input("Enter your password : ")

# validating the login 
if p1.validate_login(passw):
    while True:
        print("Bot : " + bot_responses(input(f"\n{name} : ")))
else:
    print("unable to login , please check your password")
