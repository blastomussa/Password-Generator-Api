from flask import Flask
from flask_restful import Api, Resource
from english_dictionary.scripts.read_pickle import get_dict
import random

app = Flask(__name__)
api = Api(app)



# FOR HUMAN READABLE PW GENERATION
words_dict = get_dict()
words = {}
# remove proper words from dict and add length key: value for each word to new dict
for word in words_dict:
    if word.islower():
        words.update({word: len(word)})


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

@api.resource('/generate')
class Generate(Resource):
    def get(self):
        choices = []
        for word in words:
            if words[word] == 4:
                choices.append(word)
        return {"password": random.choice(choices)}



if __name__ == '__main__':
    app.run(debug=True)
