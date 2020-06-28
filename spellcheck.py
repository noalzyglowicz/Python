import urllib.request

order = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt')

word_bank = []
word_bank_lower = []
for line in order:
    record = line.decode('UTF-8').lower().strip()
    word_bank.append(record)


user_input = 0
print("Type text; enter a blank line to end.")
while user_input != "":

    user_input = input()
    user_input_list = user_input.split()
    user_input_modified_list = []

    for word in user_input_list:
        word = word.strip().strip(".?!,()\"\'")
        user_input_modified_list.append(word)

    for word in user_input_modified_list:
        capitalized_word = word
        word = word.lower()
        if word not in word_bank:
            print("  MISSPELLED: " + capitalized_word)





