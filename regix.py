import re

text = "random string. MyName123@website.com . some more random text. YourName1344@website.com My_your-name.who@gmail.com"
#the meaning of  [ABC] is looking for a single letter a b or c
#the search function only execute for the first search if there is more words that are the same will be ignore.
#a-z is setting the range. it is case sensitive in the search function
#+ sign in the quote means "whatever come before the plus sign i can have one or more of results" space does not count![a-zA-z0-9]+ ..... \. to escape the period 
pattern = re.compile("[a-zA-z0-9\.\-\_]+\@[a-zA-z0-9]+\.[a-zA-z]+")

result = pattern.search(text)
#if you want to find everything
all_result = pattern.findall(text)
print(result)
print(all_result)