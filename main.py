import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


print('Ema: How can I assist you?')


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'hii'], single_response=True)

    response('Glad to hear that', ['good', 'fine'], single_response=True)

    response('See you!', ['bye', 'goodbye'], single_response=True)

    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'you'])

    response('You\'re welcome!', ['thanks'], single_response=True)

    response('Aww!, thanks but i\'m a bot', ['love', 'lover', 'loving', 'relation', 'relationship'],
             single_response=True)

    response('My name is Ema', ['what', 'is', 'your', 'name'], required_words=['name', 'your'])

    response('College\'s full name is Royal College of Science and Commerce', ['what', 'is', 'college', 'name'],
             required_words=['college', 'name'])

    response('I was created by two Genius, they are ABHIJEET and HIMANSHU', ['created'], single_response=True)

    response("No Royal college doesn't provide Masters or MSc.", ['masters'], required_words=['masters'])

    response("Royal college doesn't provide Masters", ['msc'], required_words=['msc'])

    response("College's Website is : http://www.royalcollegedombivli.com/profile.html", ['college', 'website'],
             required_words=['college', 'website'])

    response("Royal college comes under Mumbai University (MU)", ['university'], required_words=['university'])

    response("Dr. VivekKumar V. Patil Sir is The Principal of our COLLEGE", ['principal'],
             required_words=['principal'])

    response("Full year Fees for BSc IT is Rs 24000/-", ['bsc', 'it', 'fees'], required_words=['bsc', 'it', 'fees'])

    response("Full year Fees for BMS is Rs 20000/-", ['bms', 'fees'], required_words=['bms', 'fees'])

    response("Full year Fees for BMM is Rs 20000/-", ['bmm', 'fees'], required_words=['bmm', 'fees'])

    response("Full year Fees for BAF is Rs 18000/-", ['baf', 'fees'], required_words=['baf', 'fees'])

    response("Full year Fees for BMS is Rs 10000/-", ['bcom', 'fees'], required_words=['bcom', 'fees'])

    response("To take admission, you will require a few documents i.e\n     2-3 Passport sized photos\n     "
             "12th Mark-sheet\n     Leaving Certificate and etc.\n     "
             "For further information contact our College", ['admission'], required_words=['admission'])

    response("NO! College is against of taking donation", ['donation'], required_words=['donation'])

    response("Yes, but you should have done IT subject and Maths subject in your 12th", ['switch'], required_words=['switch'])

    # Longer Responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])

    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    response(long.R_HELP, ['contact'], required_words=['contact'])

    response(long.R_ADDRESS, ['address', 'location'], required_words=['address'])

    response(long.R_LOCATION, ['location', 'what'], required_words=['location'])

    response(long.R_COURSES, ['courses', 'structure'], required_words=['courses'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system


while True:
    print('Ema: ' + get_response(input('You: ')))
