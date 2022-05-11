from english_dictionary.scripts.read_pickle import get_dict
import random
words_dict = get_dict()


words = {}

for word in words_dict:
    if word.islower():
        words.update({word: len(word)})

string = "somerandomstring"



'''
LOC_CAPS = 'first'
if LOC_CAPS == 'first': print('first')
elif LOC_CAPS == 'last': print('last')
elif LOC_CAPS == 'random': print('random')
else: print("No Match")
'''


'''
# max and min string lengths
MAX=24
MIN=6
#number of words
NUM_WORDS=2

total = random.randrange(MIN,MAX)
# make sure 1 and 2 letter words arent chosen
n = random.randrange(3, total-2)
m = total - n
print(total)
print(n)
print(m)

#get rand word length in range of min max for num of words
i=0
lens = []
#total string length
#fucked not right
#compare numbers and spli larger again maybe till end of loop
total = random.randrange(MIN,MAX)
n = random.randrange(3, total-2)
lens.append(n)
while(i<NUM):
    n = total - n
    lens.append(n)
    i=i+1
print(lens)
'''

'''
# not working yet
string = ""
i=0
while(i<NUM):
    choices= []
    for word in words:
        if words[word] == n:
            choices.append(word)
    string = string + random.choice(choices)
    i++


# working
choices1 = []
for word in words:
    if words[word] == n:
        choices1.append(word)

choices2 = []
for word in words:
    if words[word] == m:
        choices2.append(word)

print(random.choice(choices1)+random.choice(choices2))
'''
