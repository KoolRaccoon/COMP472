# 4-5 pages report
#   - >indicate the 3rd language and why it was chosen
# 30 output files
# add the ponctuations will be a good idea for extra experimentation 


# Output Files 
#   unigramFR.txt
#   bigramFR.txt
#   unigramEN.txt
#   bigramEN.txt
#   unigramOT.txt
#   bigramOT.txt


# ie "I hate AI!!! :#"

# P(i) = 2/7 
# p(i) = (2+0.5)/(7+26*05)




######################### Unigram models #########################

# Extract Moby-dick train data
with open('TrainingCorpusENandFR/en-moby-dick.txt', 'r') as content_file:
    moby_dick_train = content_file.read()


# Extract sentences
with open("Sentences.txt", 'r') as file:
    Sentences = [line for line in file.read().split('\n')]
# print (Sentences)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
special_characters = [",", ".", ";", "-", '"', "'", ":", "?", "!"]

### Clean English Train Set ###
# Remove all spaces
moby_dick_train = ''.join(moby_dick_train.split())

# Remove all special characters
for char in special_characters:
    moby_dick_train = moby_dick_train.replace(char, '')
 

### Clean Sentences ###
clean_sentences = [None]* len(Sentences)
incrementor = 0
for line in Sentences:
    line = ''.join(line.split())

    # Remove all special characters
    for char in special_characters:
        line = line.replace(char, '')
 
    # All lowercase letters
    line = line.lower()

    clean_sentences[incrementor] = line
    incrementor = incrementor + 1
    

# print (clean_sentences)

### Count frequency of letters in English training set ###
english_letter_frequencies  = [None] * len(alphabet)
unigram_probs               = [None] * len(alphabet)
unigram_output              = [None] * len(alphabet)
incrementor                 = 0

for letter in alphabet:
    # print ("Number of " + letter + " =", moby_dick_train.count(letter))
    english_letter_frequencies[incrementor] =  moby_dick_train.count(letter)
    unigram_probs[incrementor] = english_letter_frequencies[incrementor] / len(moby_dick_train)
    unigram_output[incrementor] = "P(" + letter + ") = " +  str(unigram_probs[incrementor])
    incrementor = incrementor + 1

# print (unigram_probs)
with open('n_gram_models/unigramEN.txt', 'w') as f:
    for item in unigram_output:
        f.write("%s\n" % item)

# print ("letter frequencies: ", english_letter_frequencies)


### Count frequency of letters in sentences ###
for instance in clean_sentences:
    incrementor = 0
    Sentences_letter_frequencies    = [None] * len(alphabet)
    unigram_probs                   = [None] * len(alphabet)
    
    for letter in alphabet:
        if instance.count(letter) != 0:
            Sentences_letter_frequencies[incrementor] = instance.count(letter)
            unigram_probs[incrementor] = Sentences_letter_frequencies[incrementor] /
 

        incrementor = incrementor + 1













        

        # print ("Number of " + letter + " =", moby_dick_train.count(letter))
        english_letter_frequencies[incrementor] =  moby_dick_train.count(letter)
        incrementor = incrementor + 1

# print ("letter frequencies in sentences: ", english_letter_frequencies)



# # for spaces
# print ("Number of spaces =", moby_dick_train.lower().count(" "))
# # for comas:
# print ("Number of comas =", moby_dick_train.lower().count(","))
# # for periods
# print ("Number of periods =", moby_dick_train.lower().count("."))
# # for semi-colons
# print ("Number of semi-colons =", moby_dick_train.lower().count(";"))
# # for dashes
# print ("Number of dashes =", moby_dick_train.lower().count("-"))
# # for  quotation marks
# print ("Number of quotation marks", moby_dick_train.lower().count('"'))
# # for apostophes
# print ("Number of apostophes", moby_dick_train.lower().count("'"))
# # for colons
# print ("Number of colons", moby_dick_train.lower().count(":"))
# # for question marks
# print ("Number of question marks", moby_dick_train.lower().count("?"))
# # for exclamation marks
# print ("Number of exclamation marks", moby_dick_train.lower().count("!"))











# moby_dick_train = moby_dick_train.replace(',','')
# moby_dick_train = moby_dick_train.replace('.','')
# moby_dick_train = moby_dick_train.replace(';','')
# moby_dick_train = moby_dick_train.replace('-','')
# moby_dick_train = moby_dick_train.replace('"','')
# moby_dick_train = moby_dick_train.replace("'","")
# moby_dick_train = moby_dick_train.replace(":","")
# moby_dick_train = moby_dick_train.replace("?","")
# moby_dick_train = moby_dick_train.replace("!","")







# QUESTIONS ABOUT PROJECT
# Do the 20 extra sentences have to be in the new language only, or a mix of all 3?