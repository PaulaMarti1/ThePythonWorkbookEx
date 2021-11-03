#Ex.36 p.16
'''
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
'''

def indicate_letter(letter):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if letter in vowel:
        return 'this letter is a vowel'
    elif letter == 'y' or letter == 'Y':
        return 'this letter sometimes is a vowel but sometimes is a consonant'
    else:
        return 'this letter is a consonant'

print(indicate_letter('i'))

#Ex 67
'''
A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge. Children between 3 and
12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
for all other guests is $23.00.
Create a program that begins by reading the ages of all of the guests in a group
from the user, with one age entered on each line. The user will enter a blank line to
indicate that there are no more guests in the group. Then your program should display
the admission cost for the group with an appropriate message. The cost should be
displayed using two decimal places.
'''

age = input('please give an age\n')
list_of_age = []
cost = 0
while age != '':
    age_int = int(age)
    if age_int >= 3 and age_int <= 12:
        cost = cost + 14
    elif age_int >= 65:
        cost = cost + 18
    elif age_int > 12 and age_int < 65:
        cost = cost + 23
    else:
        cost = cost + 0
    age = (input('please give an age\n'))
print(cost)

#Ex96
'''
In this exercise you will write a function that determines whether or not a password
is good. We will define a good password to be a one that is at least 8 characters
long and contains at least one uppercase letter, at least one lowercase letter, and at
least one number. Your function should return true if the password passed to it as
its only parameter is good. Otherwise it should return false. Include a main program
that reads a password from the user and reports whether or not it is good. 
'''
def password(passw):
    l = len(passw)
    if l >= 8:
        if any(ele.isupper() for ele in passw) == True and any(ele.islower() for ele in passw) == True and any(ele.isdigit() for ele in passw) == True:
            return True
    return False
print(password("Hila12..."))

