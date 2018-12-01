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
import math

# Extract Moby-dick train data
with open('TrainingCorpusENandFR/en-moby-dick.txt', 'r') as content_file:
    moby_dick_train = content_file.read()


# Extract sentences
with open("Sentences.txt", 'r') as file:
    Sentences = [line for line in file.read().split('\n')]
# print (Sentences)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
special_characters = [",", ".", ";", "-", '"', "'", ":", "?", "!"]
languages = ["english", "french"]

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
    calculate_sentence_probability()





def calculate_unigram_probability(unigram = None, unigram_probs = None, train_corpus_len = None):
    unigram_pos = 0
    for i in range (0, len(alphabet)):
        if unigram == alphabet[i]:
            unigram_pos = i

    return float(unigram_probs[i])/float(train_corpus_len)



def calculate_sentence_probability(sentence = None, unigram_probs = None, train_corpus = None):
    for letter in sentence:
        print("UNIGRAM: ", letter)
        for language in languages:
            unigram_prob = calculate_unigram_probability(unigram = letter, unigram_probs = unigram_probs, train_corpus_len = len(train_corpus))
            sentence_log_prob += math.log(unigram_prob, 2)
            print_log_prob(language, sentence_log_prob, unigram_prob, letter)
        
        print("\n")


def print_log_prob(language = None, sentence_log_prob = None, unigram_prob = None, unigram = None):
    print (language, ": P(", unigram, ") = ", unigram_prob, " ==> log prob of sentence so far: ", sentence_log_prob)

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
# Do we combine the texts of eah languages in one input for that language?