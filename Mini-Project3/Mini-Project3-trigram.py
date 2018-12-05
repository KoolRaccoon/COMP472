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
import json

input_files = ["TrainingCorpuses/inputEN.txt", "TrainingCorpuses/inputFR.txt", "TrainingCorpuses/inputRO.txt"]
output_files = ["n_gram_models/trigramEN.txt", "n_gram_models/trigramFR.txt","n_gram_models/trigramRO.txt"]
# Extract Moby-dick train data
train_corpuses = []
for corpus in input_files:
    with open(corpus, 'r') as content_file:
        in_train = content_file.read()
    train_corpuses.append(in_train)

# Extract sentences
with open("Sentences.txt", 'r') as file:
    Sentences = [line for line in file.read().split('\n')]


### Creating the unigrams ###
total_letters = 26
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
special_characters = [",", ".", ";", "-", '"', "'", ":", "?", "!", "_", "*", "(", ")", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
languages = ["english", "french", "romanian"]

Unigram_list = alphabet

### Creating the bigrams ###
incrementor = 0
Bigram_list = [None]*(total_letters*total_letters)
for letter1 in alphabet:
    for letter2 in alphabet:
        Bigram_list[incrementor] = letter1+letter2
        incrementor = incrementor + 1

### Creating the tri-grams ###
incrementor = 0
Trigram_list = [None]*(total_letters*total_letters*total_letters)
for letter1 in alphabet:
    for letter2 in alphabet:
            for letter3 in alphabet:
                Trigram_list[incrementor] = letter1+letter2+letter3
                incrementor = incrementor + 1

### Clean Train Sets ###
for train_set in train_corpuses:
    train_set = ''.join(train_set.split())
    train_set = train_set.lower()
    # Remove all special characters
    for char in special_characters:
        train_set = train_set.replace(char, '')
 
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



### Count frequency of letters in each training set ###
letter_frequencies   = [[] for i in range(len(languages))]
n_gram_probs         = [[] for i in range(len(languages))]
n_gram_outputs       = [[] for i in range(len(languages))]
# [[[] for i in range(n)] for i in range(n)]
for i in range (0, len(languages)):
    incrementor = 0
    for letter in Trigram_list:
        letter_frequencies[i].append(train_corpuses[i].count(letter))
        n_gram_probs[i].append((letter_frequencies[i][incrementor]+1) / (len(train_corpuses[i]))+(1*len(Trigram_list)))
        n_gram_outputs[i].append("P(" + letter + ") = " +  str(n_gram_probs[i][incrementor]))
        incrementor = incrementor + 1

    # print (n_gram_probs)
    with open(output_files[i], 'w') as f:
        for item in n_gram_outputs[i]:
            f.write("%s\n" % item)

# print(n_gram_probs)

### Count frequency of letters in sentences ###
# for instance in clean_sentences:

def get_ngram_probability(character = None, n_gram_probs = None, train_corpus_len = None, n_gram_list=None, smoothing=None):
    unigram_pos = 0
    counter = 0

    for char in n_gram_list:
        if character == char:
            unigram_pos = counter 
        counter = counter + 1

    return n_gram_probs[unigram_pos]
   



def calculate_sentence_probability(Languages = None, sentence = None, n_gram_probs = None, n_gram_list=None, train_corpus = None, smoothing=None):
    sentence_log_prob = [0,0,0]
    string_outputs =[]
    language_probs = []
    for i in range (0,(len(sentence)-2)):
        n_gram = sentence[i]+sentence[i+1]+sentence[i+2]
        uni_string = "BIGRAM: "+ n_gram
        string_outputs.append(uni_string)
        # for language in languages:
        for i in range(0, len(languages)):
            letter_prob = get_ngram_probability(character = n_gram, n_gram_probs = n_gram_probs[i], n_gram_list=n_gram_list, train_corpus_len = len(train_corpus[i]), smoothing=smoothing)
            sentence_log_prob[i] = sentence_log_prob[i] + math.log(letter_prob, 10)
            string_outputs.append(print_log_prob(Languages[i], sentence_log_prob[i], letter_prob, n_gram))
            
        string_outputs.append("\n")

    max_prob = max(sentence_log_prob)
    index = sentence_log_prob.index(max_prob)
    language = Languages[index]

    return language, max_prob, string_outputs


def print_log_prob(language = None, sentence_log_prob = None, n_gram_prob = None, n_gram = None):
    return (language + ": P(" + str(n_gram) + ") = " + str(n_gram_prob) + " ==> log prob of sentence so far: " + str(sentence_log_prob))

if __name__ == "__main__":
    n_gram_list = Trigram_list
    # for idx, n_gram in enumerate(n_gram_list):
    idx = 3
    print("Answers with "+ str(idx)+ "-gram \n")
    for i in range (0, len(clean_sentences)):
        smoothing = 1
        language, max_prob, string_outputs = calculate_sentence_probability(languages, clean_sentences[i], n_gram_probs, n_gram_list, train_corpuses, smoothing)
        print ("for sentence: ",Sentences[i])
        print("Language predicted:", language, "\n")
       
        out_file = "outputs/out"+str(i+1)+".txt"
        # print(out_file)
        with open(out_file, 'w') as output_file:
            output_file.write("\n")
        for string in string_outputs:
            with open(out_file, 'a') as output_file:
                output_file.write(string + "\n")
    print("\n\n")