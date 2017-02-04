'''
Created on 24.12.2016

@author: heimo
'''
from string import punctuation
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    punctuationMarks = ('.', '?', '!', ':', ';', '-', '—', '(', ')', ' ,', ' ', '[', ']')
    #TODO Replace text if member of punctuationMarks
    text = text.casefold()
    return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")