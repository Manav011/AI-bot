import re


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
    response('You\'re welcome!', ['thank', 'thanks'], single_response = True)

    best_match = max(highest_prob_list , key = highest_prob_list.get)
    print(highest_prob_list)

    #return unknown() if highest_prob_list[best_match] < 1 else best_match
    return best_match 
    


def bot_responses(user):
    user_msg = re.split(r'\s+|[,;?!.-]\s*', user.lower())
    response = chk_msg(user_msg)
    return response

# testing response system
while True:
    print("Bot : " + bot_responses(input("You : ")))
