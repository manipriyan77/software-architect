#LIST

languages = ["Javascript","Java","Python",77,True,7.7]
print(type(languages))
print(len(languages))
languages.append("SQL")
print(languages)

languages.extend(["Reactjs","Springboot","Devops","AWS"])
print(languages)

print(languages[6])

languages.append("1321")
print(languages)
languages.remove("1321")

print(languages)

languages.append(77)
print(languages)

del languages[11] 
# del languages[-1]
print(languages)

languages.remove(77)
languages.remove(7.7)
languages.remove(True)

languages.sort()
print(languages)

languages.sort(reverse=True)

print(languages)

languages[0] = "Languages"

print(languages)

####################################################################################################################################################################################



##TUPLE

panCards =("DA2342352","FS4235363")
print(type(panCards))

print(panCards)


####################################################################################################################################################################################
#SET

colors ={"red","blue","green","red","yello","blue"}
print(colors)

votes =["a","b","a","c","a","a","b","a","c"]

print(len(votes))
print("set voters",set(votes))

marketingTeam = {'andika','casselyn','miki tong','nicklaus' ,'barbara'}
salesTeam = {'joseph','andika','zhining','sarah','nicklaus','manoj'}

## Data Analysis using Maths along with SET

# Objective: you are asked to find employees working for multiple Teams
# solution: intersection : intersection help us find common elements from set
print(marketingTeam.intersection( salesTeam ),"Intersection")
# alternative
print(marketingTeam & salesTeam)

# Objective: you are asked to prepare a final report containing names of all employees !
# solution: Union: union is used to merge 2 sets and produce a new set.

print(marketingTeam.union(salesTeam),"union")
print(marketingTeam | salesTeam ,"OR")

# Objective: you are asked to find Dedicated/Commited Employees of SALES ONLY.
# solution: difference : difference returns elements of First SET Only Excluding Commons.

print(salesTeam.difference(marketingTeam))
print(salesTeam-marketingTeam)


# Objective: you are asked to find Dedicated/Commited Employees from Both Teams.
# solution: symmetric_diffrence: it will merge set1 and set2 but excludes the common elements
print(salesTeam.union(marketingTeam),"union")
print(salesTeam.symmetric_difference(marketingTeam),"symmetric")
print(salesTeam ^ marketingTeam)

####################################################################################################################################################################################

# Dictionary
# Dictionary uses Key:Value format  to store data

## 🎯 Characteristics of Dictionary


#1. Keys cannot be repated in a Dictionary. you can repeat values.
#2. Only Immutable dataTypes can be used as KEY , you are not allowed to use Mutable DataTypes as Key.
#Immutable Types: str/int/float/bool/tuple ✅

#Mutable types: set/list/dictionary. ❌

#explanation:

#'a' : 'apple' }   here key 'a' is valid because it is string and string is immutable.

#{ ['a'] : 'apple' } here key ['a'] is Invalid because it is list and list  is mutable.


print({ 'en' : 'english' , 'hi' : 'hindi' , 'tl' : 'telugu' })

# Syntax:  {   key : value      ,           key:value       ,        key:value          }
# Dictionary Operations

usa  = {}
# Add a New Key/Pair in a Dictionary :  syntax:    dictName [ Key ] = Value

# key: 'TX'
# value : 'Texas'
usa["TX"]= "Texas"

print(usa,"usa")
# empty set.           myset = set()
# empty dic            mydict= {}
usa['CA'] ='California'
usa['IL'] ='Illinois'

# method 1:   dictName[ KeyHere ]

# 'California'

usa[ 'CA' ]

# method 2 :        dictName.get( KeyHere )
print(usa.get('CA'))
# difference
# usa['xoxo'] // Error
usa.get('xoxo')
#  .get() method also provides  a provision to produce a default value that is only
# produced when the given key is not found.

# syntax:         dict.get(  keyHere , defautlValueHere )
print(usa.get('CA' , 'Ouch! 😡 Given Key Not Found'))
print(usa.get('XOXO' , 'Ouch! 😡 Given Key Not Found'))

# Deleting Key /Pair
del usa['CA']
print(usa,"after deletion")