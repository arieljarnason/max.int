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
                output_list = make_list(wordString)

    except FileNotFoundError:
        print("File", filename, "not found", end="")
        return ()   

    return output_list

def make_list(string_in):
    
    string_out = string_in.split() #convert string to list seperated by ' '

    return string_out

def word_randomize(word):
    if len(word) <= 3:
        return word
    punctuation = ',.:;-'
    if punctuation in word:
        first, mid, end = word[0], word[1:-1], word[-2]
    else:
        first, mid, end = word[0], word[1:-1], word[-1]
        #take first and last letter from word
    
    chars = list(mid); random.shuffle(chars)
        #randomize mid section of word

    mid = ''.join(chars); word = first+mid+end
        #merge word back together
    
    return word


def scramble_string(word_string):
    list_of_words = word_string #just for clarity
    randomized_string = ''
    i = 0 #sloppy way to send each word to randomize, need to fix
    while i < len(list_of_words):
        word = list_of_words[i]
        word_randomize(word)
        i += 1 
        randomized_string += (word_randomize(word) + ' ')

    return randomized_string #convert list back to string


#MAIN PROGRAM

random.seed(10)
filename = input("Enter name of file: ")
# filename = "fathers brought us forth 'murica, yes." #delete
word_string = get_word_string(filename) #fetches string from file
scrambled_string = scramble_string(word_string) #scrambles words in string
print(scrambled_string) #prints scrambled version
