# Regular expression 

""" 

[] : Set of Characters 
eg> [a-z] a to z 
  > [b-d] b to d 
  > [A-Z] A to Z .. so on 

. : Any character except a new line 
^ : Starts with 
$ : Ends with 
* : Zero or More occurrence 
+ : one or more occurrence 
? : zero or one occurrence 
{n}: Exactly the specified number of occurrence 
| : either 
() : Capture and group

[^arn] : Except the mentioned set 

"""

# Let's apply these regex using python 

import re

txt = "wow heel hostel hall hell hero honda"

# findall : Return the list of all the words matching the pattern 
print(re.findall("^h*", txt))

# search : Return an object of all mathches 
print(re.search('^h*', txt))

# split: Returns a list of splitted txt where pattern matches 
print(re.split('h', txt))

# sub: Replace the match with your choice: return a string  
print(re.sub('h', 'p', txt))

