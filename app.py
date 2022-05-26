# v1.0
# vanilla flask
from flask import Flask, json, jsonify, request, render_template
from english_dictionary.scripts.read_pickle import get_dict
import random

app = Flask(__name__)

# this is the entry point for wsgi
application = app

SPECS_LIST = ["!","@","#","$","%","^","&","*","_","+","-","=","?","<",">","|"]
WORDS = []
LENGTHS = {}
# Build GLOBAL length dictionary and word list
words_dict = get_dict()
for word in words_dict:
    if word.islower(): #only match lower case words
        WORDS.append(word)
        LENGTHS.update({word:len(word)})


#NOT WORKING YET
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
  return render_template("404.html")


#WORKING
@app.route('/')
def help():
    return render_template("help.html")

#WORKING
@app.route('/api/v1', methods=['GET','PUT','POST','DELETE'])
def generate_pw():
    method = request.method
    bad_request = False
    choices = set(('first','last','random'))
    if method == 'GET':
        # GET PARAMETERS AND VALIDATE USER INPUT
        max = request.args.get('max', default = 18, type = int)
        min = request.args.get('min', default = 8, type = int)
        if max > 100 or max < min: bad_request = True
        if min < 0 or min > max: bad_request = True

        num_words = request.args.get('num_words', default = 2, type = int)
        if num_words < 0 or num_words > 25: bad_request = True

        caps = request.args.get('caps', default = True, type = bool)
        num_caps = request.args.get('num_caps', default = 1, type = int)
        if num_caps < 0 or num_caps > max: bad_request = True
        loc_caps = request.args.get('loc_caps', default = 'first', type = str).lower()
        if loc_caps not in choices:
            bad_request = True

        ints = request.args.get('ints', default = True, type = bool)
        num_ints = request.args.get('num_ints', default = 2, type = int)
        if num_ints < 0 or num_ints > max: bad_request = True
        loc_ints = request.args.get('loc_ints', default = 'last', type = str).lower()
        if loc_ints not in choices:
            bad_request = True

        specs = request.args.get('specs', default = True, type = bool)
        num_specs = request.args.get('page', default = 1, type = int)
        if num_specs < 0 or num_specs > max: bad_request = True
        loc_specs = request.args.get('loc_specs', default = 'last', type = str).lower()
        if loc_specs not in choices:
            bad_request = True

        gib = request.args.get('gib', default = False, type = bool)

        if bad_request == False:
            # build password from given parameters
            string = get_words(max, min, num_words, num_ints, num_specs)
            if caps: string = add_caps(string, num_caps, loc_caps)
            if string != "No password could be generated with the given parameters":
                if ints: string = add_ints(string, num_ints, loc_ints)
                if specs: string = add_specs(string, num_specs, loc_specs)
                if gib: string = gibberish(string)
            # create response json and status_code
            response = jsonify({'password': string})
            response.status_code = 200
            return response
        else:
            response = jsonify({'Bad request': 'Check that parameters are within acceptable range'})
            response.status_code = 400
            return response
    else:
        response = jsonify({"Method not found": "The method is not allowed for the requested URL. This endpoint only responds to GET requests."})
        response.status_code = 405
        return response


#Concat random words and make sure final string is in MIN/MAX range
def get_words(max, min, num_words, num_ints, num_specs):
    i = 0
    string = ''
    total_length = num_ints + num_specs
    iterations = 0
    while i < num_words:
        i = i + 1
        word = random.choice(WORDS)
        string = string + word
        total_length = total_length + LENGTHS[word]
        # reset and try again if string is too long
        if total_length > max or total_length < min:
            iterations = iterations + 1
            string = ''
            i = 0
            total_length = num_ints + num_specs
            if iterations == 10000: # prevent endless looping; tries 10000 word combos
                string = "No password could be generated with the given parameters"
                break
    return string


# add capital letters to password string
def add_caps(string, num_caps, loc_caps):
    i = 0
    start = 0
    end = -1
    while i < num_caps:
        i = i + 1
        if loc_caps.lower() == 'first':
            string = string.replace(string[start],string[start].upper(),1)
        elif loc_caps.lower() == 'last':
            # sometimes matches earleir character than the last, hmmm whats the solution
            string = string.replace(string[end],string[end].upper(),1)
        elif loc_caps.lower() == 'random':
            length = len(string)
            index = random.randrange(length)
            string = string.replace(string[index],string[index].upper(),1)
        else: pass
        start = start + 1
        end = end - 1
    return string


# add integers to password string
def add_ints(string, num_ints, loc_ints):
    # build approriate range
    i = 0
    range = 1
    while i < num_ints:
        i = i + 1
        range = range * 10
    integer = random.randrange((range/10),range)
    if loc_ints.lower() == 'first':
        string = str(integer) + string
    elif loc_ints.lower() == 'last':
        string = string + str(integer)
    elif loc_ints.lower() == 'random':
        for int in str(integer):
            length = len(string)
            index = random.randrange(length)
            string = string[:index] + int + string[index:]
    else: pass
    return string


# add special characters from specified list
def add_specs(string, num_specs, loc_specs):
    i = 0
    while i < num_specs:
        i = i + 1
        char = random.choice(SPECS_LIST)
        if loc_specs.lower() == 'first': string = char + string
        elif loc_specs.lower() == 'last': string = string + char
        elif loc_specs.lower() == 'random':
            length = len(string)
            index = random.randrange(length)
            string = string[:index] + char + string[index:]
        else: pass
    return string


# scramble string randomly to create gibberish
def gibberish(string):
    l = len(string)
    for c in string: #switch characters in string randomly
        index = random.randrange(l)
        r = string[index]
        string = string.replace(c,r,1)
        string = string.replace(r,c,1)
    return string

# host='0.0.0.0' required to run inside docker image
if __name__ == '__main__':
    app.run(host='0.0.0.0')
