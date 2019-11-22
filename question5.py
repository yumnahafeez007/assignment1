#Write a Python program which accepts the user's first and last name and
#print them in reverse order with a space between them.


first = input('Enter First name: ')
last = input('Enter Last name: ')

len_first =  len(first)
reverse_first = first[len_first::-1]

len_last =  len(last)
reverse_last = last[len_last::-1]


print(reverse_first+' '+reverse_last)