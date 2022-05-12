from flask import Flask, request
from flask_restful import Api, Resource
from english_dictionary.scripts.read_pickle import get_dict
import random

app = Flask(__name__)
api = Api(app)

# this is the entry point
application = app

MAX = 16
MIN = 4
NUM_WORDS=2
CAPS = True
NUM_CAPS = 1
LOC_CAPS = 'first' #first, random, last
INTS = True
NUM_INTS = 2
LOC_INTS = 'last' #first, last, random
SPECS = True
NUM_SPECS = 1
LOC_SPECS = 'last' #first, last, random
SPECS_LIST = ["!","@","#","$","%","^","&","*","_","+","-","=","?","<",">","|"]
SUBS = False
GIB = False
WORDS = []
LENGTHS = {}
# Build GLOBAL length dictionary and word list
words_dict = get_dict()
for word in words_dict:
    if word.islower(): #only match lower case words
        WORDS.append(word)
        LENGTHS.update({word:len(word)})

# API Resource
@api.resource('/')
class Generate(Resource):
    def get(self):
        self.get_parameters()
        self.get_words()
        self.add_caps()
        self.add_ints()
        self.add_specs()
        self.add_subs()
        self.gibberish()
        pw = self.string
        self.reset_defaults()
        return {"password": pw}

    def get_parameters(self):
        # Is there a better way to set defaults for paremeters than global vars?
        global MAX, MIN, NUM_WORDS, CAPS, NUM_CAPS, LOC_CAPS, INTS, NUM_INTS, LOC_INTS, SPECS, NUM_SPECS, LOC_SPECS, SPECS_LIST, SUBS, GIB
        if request.args.get('MAX'): MAX = int(request.args.get('MAX'))
        if request.args.get('MIN'): MIN = int(request.args.get('MIN'))
        if request.args.get('NUM_WORDS'): NUM_WORDS = int(request.args.get('NUM_WORDS'))
        if request.args.get('CAPS'): CAPS = bool(request.args.get('CAPS'))
        if request.args.get('NUM_CAPS'): NUM_CAPS = int(request.args.get('NUM_CAPS'))
        if request.args.get('LOC_CAPS'): LOC_CAPS = str(request.args.get('LOC_CAPS'))
        if request.args.get('INTS'): INTS = bool(request.args.get('INTS'))
        if request.args.get('NUM_INTS'): NUM_INTS = int(request.args.get('NUM_INTS'))
        if request.args.get('LOC_INTS'): LOC_INTS = str(request.args.get('LOC_INTS'))
        if request.args.get('SPECS'): SPECS = bool(request.args.get('SPECS'))
        if request.args.get('NUM_SPECS'): NUM_SPECS = int(request.args.get('NUM_SPECS'))
        if request.args.get('LOC_SPECS'): LOC_SPECS = str(request.args.get('LOC_SPECS'))
        if request.args.get('SUBS'): SUBS = bool(request.args.get('SUBS'))
        if request.args.get('GIB'): GIB = bool(request.args.get('GIB'))


    def get_words(self):
        #Concat random words and make sure final string is in MIN/MAX range
        i = 0
        self.string = ''
        total_length = NUM_INTS + NUM_SPECS
        while i < NUM_WORDS:
            i = i + 1
            word = random.choice(WORDS)
            self.string = self.string + word
            total_length = total_length + LENGTHS[word]
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
                    # sometimes matches earleir character than the last, hmmm whats the solution
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
            integer = random.randrange((range/10),range)
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
        #substitute characters in string; leet
        if SUBS == True:
            pass


    def gibberish(self):
        #scramble string
        if GIB == True:
            l = len(self.string)
            for c in self.string:
                #switch characters in string randomly
                index = random.randrange(l)
                r = self.string[index]
                self.string = self.string.replace(c,r,1)
                self.string = self.string.replace(r,c,1)


    def reset_defaults(self):
        global MAX, MIN, NUM_WORDS, CAPS, NUM_CAPS, LOC_CAPS, INTS, NUM_INTS, LOC_INTS, SPECS, NUM_SPECS, LOC_SPECS, SPECS_LIST, SUBS, GIB
        MAX = 16
        MIN = 4
        NUM_WORDS=2
        CAPS = True
        NUM_CAPS = 1
        LOC_CAPS = 'first' #first, random, last
        INTS = True
        NUM_INTS = 2
        LOC_INTS = 'last' #first, last, random
        SPECS = True
        NUM_SPECS = 1
        LOC_SPECS = 'last' #first, last, random
        SUBS = False
        GIB = False
        self.string = ''


if __name__ == '__main__':
    app.run()

# ADD
    # POST/PUT/DELETE error handling
    # Return codes
    # throttling
    # bulk? json output; add endpoint
    # how do I run app on namecheap host under blastomussa.dev domain?
        # fucked up; tear down try again, find better instructions
