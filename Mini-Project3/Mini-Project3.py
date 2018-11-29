# 4-5 pages report
# 	- >indicate the 3rd language and why it was chosen
# 30 output files
# add the ponctuations will be a good idea for extra experimentation 

# ie "I hate AI!!! :#"

# P(i) = 2/7 
# p(i) = (2+0.5)/(7+26*05)


with open('TrainingCorpusENandFR/en-moby-dick.txt', 'r') as content_file:
    Moby_Dick_Train = content_file.read()


# print(len(Moby_Dick_Train))
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Remove all spaces
Moby_Dick_Train = ''.join(Moby_Dick_Train.split())

for letter in alphabet:
	print ("Number of " + letter + " =", Moby_Dick_Train.lower().count(letter))
	
# for spaces
print ("Number of spaces =", Moby_Dick_Train.lower().count(" "))
# for comas:
print ("Number of comas =", Moby_Dick_Train.lower().count(","))
# for periods
print ("Number of periods =", Moby_Dick_Train.lower().count("."))




# print ("Number of b =", format(Moby_Dick_Train.count('b')))

# int counter = 0
# for i in range (0,len(Moby_Dick_Train)):
# 	a = Moby_Dick_Train[i]
# 	counter = counter + 1




# Output Files 
#	unigramFR.txt
# 	bigramFR.txt
# 	unigramEN.txt
#	bigramEN.txt
# 	unigramOT.txt
#	bigramOT.txt