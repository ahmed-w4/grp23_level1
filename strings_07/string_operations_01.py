# show strings functions
print('---- Create and print string ----')
student_name = 'AhmedWael'
code = '434234321'
print(student_name)
print(type(student_name))

print('-------- upper(), lower() functions -------------')
upper_name = student_name.upper()
lower_name = student_name.lower()
print(upper_name, lower_name, student_name)

print('------ isupper(), islower(), isalpha() functions --- True , False --')
print(upper_name.isupper())
print(lower_name.islower())
print(student_name.isalpha()) # letters only no special characters
print(student_name.isalnum()) # letters or numbers no special characters
print(code.isdigit())

print('-------------- endsWith() function -----------------')
file_path = 'c:\\my_files\\egypt.pNg'
print(file_path)
file_path = file_path.lower()

if file_path.endswith('jpg') or file_path.endswith('png'):
    print('this is an image')
elif file_path.endswith('mp3'):
    print('this is a sound')
elif file_path.endswith('mp4'):
    print('this is a video')

print('-------------- startswith() function ---------')
phone_num = '01551501509'
if phone_num.startswith('010'):
    print('vodafone user')
elif phone_num.startswith('012'):
    print('orange user')
elif phone_num.startswith('011'):
    print('etisalat user')
elif phone_num.startswith('015'):
    print('we user')
else:
    print('unkown')

print('------ in membership --------------')
emp_cv = 'iam a programmer, iam interest in java and python .'
if 'python' in emp_cv and 'java' in emp_cv:
    print('I found the wanted one ')
else:
    print('not found yet')

print('-------------- count function a word - count times of occurence -----------')
emp_cv = 'iam a python programmer, iam interest in java and python .'
print(emp_cv.count('python'))

print('---------- index(),  replace() functions |  slicing---------------')
student_email = 'ali.wael.mostafa@gmail.com'
user_name = student_email[0:student_email.index('@')]             # ahmed.wael
domain_name = student_email[student_email.index('@') + 1:]          # gmail.com
real_name = user_name.replace('.', ' ')
print(user_name, domain_name, real_name)

print('--------------- Looping :  Loop over letters of string -----------------------')
for i in range(len(real_name)): # for i index loop      = slicing
    print(real_name[i])
print('----- for each loop --- ')
for letter in real_name:
    print(letter)

print('------- Split function the String into List of Words -------')
my_courses = 'oracle java python php asp mysql'
words_list = my_courses.split()
print(words_list)
words_list.reverse()
print(words_list)

print('------ return the list back to string using join() function --------')
new_courses = ' '.join(words_list)
print(new_courses)

print('---------- strip(), title(), swapcase(), find(), rfind() Self study   -------------------')
# strip() is used to remove any leading and trailing special characters or space
text = ",,,Hello,,,World!!!,,,"
stripped_text = text.strip(",!")
print(stripped_text) # Output: "Hello,,,World"

# title() makes first letter of every new word a capital letter
sentence = "hello world"
print(sentence.title()) # Output: Hello World

# swapcase makes capital small and vice versa
text = "Python Is Awesome!"
print(text.swapcase()) # Output: "pYTHON iS aWESOME!"

#  find() is used to search for the first occurrence of a specified value within a string
sentence_2 = "This is a sample sentence."
index = sentence_2.find("sample")
print(index) # Output: 10

# rfind() returns the highest index of the substring if it is found in the given string
text = "Python is fun, isn't it? Fun to learn, fun to play with."
index = text.rfind('fun')
print(index) # Output: 37