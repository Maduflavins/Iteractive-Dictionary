import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
import json
data = json.load(open("data.json"))

def  word_meaning(w):
    word = word.lower()
    if word in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("did you mean %s instead enter Y if yes and N if no" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return get_close_matches(w, data.keys())[0]
        elif yn == "N":
            return "sorry word does not exist please recheck your spelling"
        else:
            return "we did not understand your entry"
    else:
        return "sorry the word does not exist. Please check your spelling"
word = input("enter word: ")

output = (word_meaning(w))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
