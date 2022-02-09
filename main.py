import random
import dictionary as d

def check_letter_position(word, letter, position):
    return  word.rfind(letter) == position

def check_letter(word, letter):
    return letter in word

def generate_word(dictionary):
    word = ''
    while (len(set(word)) != 5):
        word = dictionary[random.randint(0, len(dictionary)-1)]
    return str(word)

def play():
    dictionary = d.get_dictionary()
    print('Lets play')
    word_gen = generate_word(dictionary)
    print('Generated word: ', word_gen)
    
    while True:
        word_gen = input('Enter word: ')
        flags = input('Enter flags: ')
        i = 0
        for flag in flags:
            # g - green - is in the word in this position
            # y - yellow - is in the word, wrong position
            # r - red - is not in the word
            if flag == 'g':
                dictionary = [ word for word in dictionary if check_letter_position(word, word_gen[i], i) ]
            if flag == 'y':
                dictionary = [ word for word in dictionary if (check_letter(word, word_gen[i])) ]
                dictionary = [ word for word in dictionary if not(check_letter_position(word, word_gen[i], i)) ]
            if flag == 'r':
                dictionary = [ word for word in dictionary if not(check_letter(word, word_gen[i]))]
            i = i+1
        print('Try this: ', dictionary)
    
play()