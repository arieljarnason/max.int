import random
import string

#FUNCTIONS

def get_word_string(filename):
    """Opens text file"""

    wordString = ''	# start with an empty string of words 

    try:
        with open(filename, 'r', encoding='utf-8') as dataFile:
            for line in dataFile: 
                wordString += line # add each line of words to the word string 
                output_list = make_list(wordString) # use the "make_list" function to... 
                                                    # ...create list out of strings

    except FileNotFoundError:
        print("File", filename, "not found", end="") 
        return ()   

    return output_list

def make_list(string_in):
    """Converts string to list seperated by spaces"""
    newlist = string_in.split() 

    return newlist

def word_randomize(word):
    if len(word) <= 3:
        return word
        #don't bother with short words
    punctuation = ',.:;-'
    if punctuation in word:
        first, mid, end = word[0], word[1:-1], word[-2]
        #take first and last, as well as the punctuation
    else:
        first, mid, end = word[0], word[1:-1], word[-1]
        #take first and last letter from word
    
    chars = list(mid); random.shuffle(chars)
        #randomize mid section of word

    mid = ''.join(chars)
        #merge word back together
    
    return first+mid+end


def scramble_string(word_string):
    list_of_words, randomized_string, i = word_string, '', 0 
    #just for clarity, rename the list "list of words"
    #sloppy way to send each word to randomize
    
    while i < len(list_of_words):
        word = list_of_words[i]
        word_randomize(word)
        i += 1 
        randomized_string += (word_randomize(word) + ' ')
        # send each word to randomize function
        # convert list back to string

    return randomized_string 

#MAIN PROGRAM

random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename) #fetches string from file
scrambled_string = scramble_string(word_string) #scrambles words in string
print(scrambled_string) #prints scrambled version