import load_dictionary

word_list = load_dictionary.load('/Users/willyu/dev/Teaching-Python-Code/Python-Class-Level-8/2of4brif.txt')

anagram_list = []

name = 'stop'
print("Input name = {}".format(name))

name_sorted = sorted(name)
for word in word_list:
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

            