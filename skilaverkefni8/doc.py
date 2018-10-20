import string

def get_input(user_prompt):
    # user_input = input(user_prompt)
    user_input = "ap_docs2.txt"
    return user_input

def read_file(file_name):
    try:
        file_content = open(file_name, "r")
        return file_content
    except FileNotFoundError:
        print("Documents not found.")

def print_menu(user_quits):
    
    while user_quits == 0:

        print("""What would you like to do?
1. Search Documents
2. Print Document
3. Quit Program""")
        
        try:
            user_choice = int(input())

            if user_choice == 1:
                return user_choice  #run search document
            elif user_choice == 2:
                return user_choice  #run print document
            elif user_choice == 3:
                user_quits = 1      #quits program
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")

def create_string_from_data(file):
    whole_file_string = ''
    list_of_longstrings = []
    for line in file:
        whole_file_string += line
    return whole_file_string

def clean_strings(doc_content):

    #strip all words within all strings in line_list of punctuation
    word_list = doc_content.split( )

            #LAGA
    word_list = ([s.replace('.', "") for s in word_list])
    word_list = ([s.replace(',', "") for s in word_list])
    word_list = ([s.replace("'", "") for s in word_list])
    word_list = ([s.replace("`", "") for s in word_list])
    word_list = ([s.replace(" ", "") for s in word_list])
    word_list = ([s.replace("_", "") for s in word_list])
    word_list = ([s.replace("-", "") for s in word_list])

    #make new long string without "." and ","
    new_long_string = ''
    for item in word_list:
        new_long_string += item+" "
   
    #2 x lists of documents in long strings
    clean_line_list = new_long_string.split("<NEW DOCUMENT>"); clean_line_list.remove("")
    org_list = doc_content.split("<NEW DOCUMENT>"); org_list.remove("")
    
    #line_list is now a list of long strings with no punctuation, each item
    #in the list is one document
    #org_list is for printing
    return clean_line_list, org_list

def make_dictionary(clean_list_of_strings):
    """Makes dictionary out of a list of long strings of clean words"""
    #take clean list of strings(documents) and make a new list of words
    # seperated by " "
    # print(clean_list_of_strings)
    wordset = set(); wordlist = ''; mydict = {}
    key = ''
    #run new wordlist through set and make set of unique words
    for items in clean_list_of_strings:
        i = 0; wordlist = str(items).split()
        while i < len(wordlist):
            word = wordlist[i].lower()
            wordset.add(word)
            key = word
            mydict.setdefault(key, [])
            mydict[key].append(clean_list_of_strings.index(items))
            i+=1
    clean_word_dict = mydict
    #make dictionary from these words
    #search in dictionary for user input search
    #return word + value
    return clean_word_dict

def run_function(user_choice, clean_words_dict, org_strings):
    """Runs either the Search function or Print function based on user input"""
    if user_choice == 1:
        search_document(clean_words_dict)
        main()
    elif user_choice == 2: 
        print_document(org_strings)
        main()

def search_document(clean_words_dict):
    """Enter search words
    searches the word_dict dictionary for the words(keys)
    returns the #Document (position in list of documents)(value)
    """
    search_words = []; found_docs = set(); i=0
    search_words = input("Enter search words: ").split(" ")
    while i < len(search_words):
        found_docs = set((clean_words_dict.get(search_words[i])))
        i+=1
    found_docs = sorted(found_docs)
    found_docs = str(found_docs).replace(",","")

    # found_docs = sorted(found_docs)
    print("Documents that fit search:", (str((found_docs)[1:-1])))
    print("")

def print_document(file):
    doc_num = int(input("Enter document number: "))
    print("Document #"+str(doc_num))
    print(file[doc_num])
    
def main():
    user_quits = 0
    file_name = get_input("Document collection:" )
    file_content = read_file(file_name)
    
    if file_content: 
        user_choice = print_menu(user_quits)
        doc_content = create_string_from_data(file_content)
        file_content.close()
        clean_list_of_strings, org_strings = clean_strings(doc_content)
        clean_word_dict = make_dictionary(clean_list_of_strings)
        run_function(user_choice, clean_word_dict, org_strings)

main()