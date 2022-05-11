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
NUM_CAPS = 2
LOC_CAPS = 'random' #first, random, last

#integers
INTS = True
NUM_INTS = 4
LOC_INTS = 'last' #first, last, random

#Special Characters
SPECS = True
NUM_SPECS = 1
LOC_SPECS = 'last' #first, last, random
SPECS_LIST = ["!","@","#","$","%","^","&","*","_","+","-","=","?","<",">","|"]

#Substitute Characters
SUB = False

# Build length dictionary and word list
words_dict = get_dict()
lengths = {}
words = []
for word in words_dict:
    if word.islower(): #only match lower case words
        words.append(word)
        lengths.update({word:len(word)})

# API Resource
@api.resource('/generate')
class Generate(Resource):
    # demo
    def get(self):

        self.get_words()
        self.add_caps()
        self.add_ints()
        self.add_specs()
        self.add_subs()

        return {"password": self.string}


    def get_words(self):
        #Concat random words and make sure final string is in MIN/MAX range
        i = 0
        self.string = ''
        total_length = NUM_INTS + NUM_SPECS
        while i < NUM_WORDS:
            i = i + 1
            word = random.choice(words)
            self.string = self.string + word
            total_length = total_length +lengths[word]
            # reset and try again if string is too long
            if total_length > MAX or total_length < MIN:
                self.string = ''
                i = 0
                total_length = NUM_INTS + NUM_SPECS


    def add_caps(self):
        if CAPS == True:
            i = 0
            start = 0
            end = -1
            while i < NUM_CAPS:
                i = i + 1
                if LOC_CAPS == 'first':
                    self.string = self.string.replace(self.string[start],self.string[start].upper(),1)
                elif LOC_CAPS == 'last':
                    self.string = self.string.replace(self.string[end],self.string[end].upper(),1)
                elif LOC_CAPS == 'random':
                    length = len(self.string)
                    index = random.randrange(length)
                    self.string = self.string.replace(self.string[index],self.string[index].upper(),1)
                else: pass
                start = start + 1
                end = end - 1


    def add_ints(self):
        if INTS == True:
            # build approriate range
            i = 0
            range = 1
            while i < NUM_INTS:
                i = i + 1
                range = range * 10
            integer = random.randrange(range)
            # elif switch for integer location
            if LOC_INTS == 'first':
                self.string = str(integer) + self.string
            elif LOC_INTS == 'last':
                self.string = self.string + str(integer)
            elif LOC_INTS == 'random':
                for int in str(integer):
                    length = len(self.string)
                    index = random.randrange(length)
                    self.string = self.string[:index] + int + self.string[index:]
            else: pass


    def add_specs(self):
        if SPECS == True:
            i = 0
            while i < NUM_SPECS:
                i = i + 1
                char = random.choice(SPECS_LIST)
                if LOC_SPECS == 'first': self.string = char + self.string
                elif LOC_SPECS == 'last': self.string = self.string + char
                elif LOC_SPECS == 'random':
                    length = len(self.string)
                    index = random.randrange(length)
                    self.string = self.string[:index] + char + self.string[index:]
                else: pass


    def add_subs(self):
        pass


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
