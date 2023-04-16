import re
import details
import random


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "What does that mean?",
                "Sorry for inconvinience but i was not able to understand \n      what do you want to say can you repeat"][
        random.randrange(4)]
    return response

def msg_prob(user_inp , recognised_words , single_resp = False , required_words = []):
    msg_certainity = 0
    has_required_words = True

    # if the word in user written text is present in recognised_words then increasing message certainity 
    # means it's more accurate sentence
    for word in user_inp: 
        if word in recognised_words:
            msg_certainity += 1

    percentage = float(msg_certainity) / float(len(recognised_words))

    for word in required_words:
        if word not in user_inp:
                has_required_words = False
                break

    if required_words or single_resp:
        return int(percentage*100)
    
    else: return 0

def chk_msg(user_msg):
    highest_prob_list = {}

    def response(bot_resp , list_of_words , single_response = False , required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_resp] = msg_prob(user_msg , list_of_words , single_response , required_words)
    
    #Responses
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'hola'], single_response = True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!\n      How can I help you today', ['thank', 'thanks'], single_response = True)
    response(f"Sure , Your current balance is {p1.chk_balance()} Rs",['can' , 'check' , 'my' ,'balance'] , required_words = ['my' , 'balance'] )
    response(f"Account status = {p1.acc_stat()},\n      Account activation = {p1.acc_act()},\n      Account type = {p1.acc_type()}\n      To know more you can contact us on Toll free number :- 1800-564-9548" ,[ 'some','provide','details', 'information' , 'my' , 'account'] , required_words=['details' , 'information'])
    response(f"Account status = {p1.acc_stat()}" , ['what' , 'status' , 'account'] , required_words=['status' , 'account'])
    response(f"Account activation date = {p1.acc_act()}" , ['what','is','activation' , 'date','acocount'] , required_words=['activation' , 'what'])
    response(f"Please check this out on our web https://abcbank.com" , ['can','you','about','loans','your','bank','provide'] , required_words=['loans'])
    response(f"You can contact us on Toll free number :- 1800-564-9548" , ['can','provide','your' , 'customer care'] , required_words=['customer care'])

    best_match = max(highest_prob_list , key = highest_prob_list.get)
    # print(highest_prob_list)

    return unknown() if highest_prob_list[best_match] < 1 else best_match
    # return best_match 
    


def bot_responses(user):
    user_msg = re.split(r'\s+|[,;?!.-]\s*', user.lower())
    response = chk_msg(user_msg)
    return response



# testing response system

name , id = input("Enter your name and user id: ").split()
p1 = details.Acc_Detail(name , id)
passw = input("Enter your password : ")

if p1.validate_login(passw):
    while True:
        print("Bot : " + bot_responses(input(f"\n{name} : ")))
else:
    print("unable to login , please check your password")
