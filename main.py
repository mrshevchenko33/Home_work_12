import string

my_string = input('Enter your hashtag: ')

my_lst = my_string.split()
my_lst = [''.join(i for i in word if i not in string.punctuation) for word in my_lst]

new_string = ''.join(word.capitalize() for word in my_lst if word)

if len(new_string) > 140:
    new_string = new_string[:139]

print('#' + new_string)



