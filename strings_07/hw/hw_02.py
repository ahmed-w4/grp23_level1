str_1 = 'python exercises solution practice'

str_1 = str_1.title()
print(str_1)

word_list = str_1.split()

word_list2 = []

for item in word_list:
    letter = item[-1].upper()
    new_word = item[0:-1]
    new_word2 = new_word + letter
    print(new_word2)
    word_list2.append(new_word2)

print(word_list2)
str_1 = ' '.join(word_list2)
print(str_1)