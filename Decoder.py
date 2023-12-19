from collections import Counter

# dictionary.get
# classic dictionary no function
def counted(s):
    lets = s.split()

    h = {}
    for k, v in Counter(s).items():
        h[k] = v
    return(h)
    # refer to the google docs

def sorter(counted_dictionary):
    # this function is given!
    list_of_tuples = sorted(counted_dictionary.items(), key=lambda x: (x[1]))
    return(list_of_tuples)

def ciphered(list_of_tuples):
    d = {}

    # refer to the google docs
    for i in range(len(list_of_tuples)):
        key = list_of_tuples[i][0]
        value = list_of_tuples[len(list_of_tuples) - i - 1][0]
        d[key] = value
    return(d)

def solver(word):
    counted_dictionary = counted(word)  # dictionary of all the counts
    list_of_tuples = sorter(counted_dictionary)  # tuples of all the dictionary elements sorted
    cipher = ciphered(list_of_tuples)  # cipher (dictionary)
    d = cipher
    new_word = ""
    for i in word:
        key = i
        value = d[key]
        new_word += value
    return new_word

word = "em cd rom"

reader = open('EnCoded.txt', 'r')
writer = open('DeCoded.txt', 'w')

line = reader.readline()
while line:
    clean_line = line.strip('\n')
    print(solver(clean_line), file=writer)
    line = reader.readline()
reader.close()
writer.close()
