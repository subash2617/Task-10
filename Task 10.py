#1.check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
import re
def char(string):
    charRe=re.compile(r'[^a-zA-Z0-9.]')
    string=charRe.search(string)
    return not bool(string)
print("ABCabc123")
print(char("ABCabc123"))
print("*&%@#!")
print(char("*&%@#!"))
#2.matches a word containing 'ab'
import re
def text_match(text):
        if re.search('\w*ab.\w*',text):
                return 'matched'
        else:
                return('Not matched')
str=input()
print(text_match(str))
#3.check for a number at the end of a word/sentence
def number_check(string):
    if re.search(r'\d+s',string):
        return 'yes'
    else:
        return 'no'
str1=input()
print(number_check(str1))
#4.search the number (0-9) of length between 1 to 3 in a given string
import re
result=re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3:")
for n in result:
    print(n.group(0))
#5.match a string that contains only uppercase letters
import re
def text_match(text):
        pattern='^[A-Z]'
        if re.search(pattern,text):
                return 'matched'
        else:
                return 'Not matched'
print(text_match("hello world"))
print(text_match("Python"))