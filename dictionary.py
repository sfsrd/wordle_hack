import nltk
from nltk.corpus import words

def get_dictionary():
    # download the dictionary for the first usage
    # nltk.download('words')

    dict = words.words()
    dict = [ word for word in dict if len(word)==5 ]
    dict =  [ word.lower() for word in dict ]
    dict  = list(set(dict))
    return dict

dict = get_dictionary()