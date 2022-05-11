from flask import Flask
from flask_restful import Api, Resource
from english_dictionary.scripts.read_pickle import get_dict
import random

app = Flask(__name__)
api = Api(app)

#DEFAULT VALUES
# max and min string lengths
MAX=16
MIN=6

#number of words
NUM_WORDS=2

#Capital letters
CAPS = True
NUM_CAPS = 1
LOC_CAPS = 'first' #first, random, last

#integers
INTS = True
NUM_INTS = 4
LOC_INTS = 'last' #first, last, random

#Special Characters
SPECS = True
NUM_SPECS = 1
LOC_SPECS = 'last' #first, last, random
SPECS_LIST = ["!","@","#","$","%","^","&","*","_","+","-","=","?","<",">","|"]

#Replace Characters
REP = False

# Build length dictionary and word list
words_dict = get_dict()
lengths = {}
words = []
# remove proper words from list
for word in words_dict:
    if word.islower():
        words.append(word)
        lengths.update({word: len(word)})

# API Resource
@api.resource('/generate')
class Generate(Resource):
    # demo
    def get(self):

        #Concat random words and make sure final string is in MIN/MAX range
        i = 0
        string = ''
        total_length = NUM_INTS + NUM_SPECS
        while i<NUM_WORDS:
            i = i + 1
            word = random.choice(words)
            string = string + word
            total_length = total_length +lengths[word]
            # reset and try again if string is too long
            if total_length > MAX or total_length < MIN:
                string = ''
                i = 0
                total_length = NUM_INTS + NUM_SPECS

        #Add Capitols
        if CAPS == True:
            if LOC_CAPS == 'first':
                print('first')
            elif LOC_CAPS == 'last':
                print('last')
            elif LOC_CAPS == 'random':
                print('random')
            else:
                print("No Match")

        #Add Integers
        if INTS == True:
            # build approriate range
            i = 0
            range = 1
            while i < NUM_INTS:
                i=i+1
                range = range * 10
            integer = random.randrange(range)
            # elif switch for integer location
            if LOC_INTS == 'first': string = str(integer) + string
            elif LOC_INTS == 'last': string = string + str(integer)
            elif LOC_INTS == 'random':
                for int in str(integer):
                    length = len(string)
                    index = random.randrange(length)
                    string = string[:index] + int + string[index:]
            else: pass


        #Add Special Characters
        if SPECS == True:
            i = 0
            while i < NUM_SPECS:
                i = i + 1
                char = random.choice(SPECS_LIST)
                if LOC_SPECS == 'first': string = char + string
                elif LOC_SPECS == 'last': string = string + char
                elif LOC_SPECS == 'random':
                    length = len(string)
                    index = random.randrange(length)
                    string = string[:index] + char + string[index:]
                else:
                    print("No Match")

        #Replace characters
        if REP == True:
            pass

        return {"password": string}


if __name__ == '__main__':
    app.run(debug=True)



    #needs UTF or ASCII switch and defaults
    #needs special character switch
    #needs good random module
    #needs good english dictionary
    #needs string len min and max
    #human readable or gibberish
        #number of words
    #number of upper and lower
    #number of special chacters
    #number of integers
    #choose where uppercase letters are; beginning, end, random
    #needs defaults for everything; call with no variables should work
    #no puts/deletes/posts only get
    #api throttling so I dont get DOSed
    #bulk; output csv for download
    #how do I run app on namecheap host under blastomussa.dev domain?
