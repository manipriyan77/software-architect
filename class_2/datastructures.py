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





##TUPLE

panCards =("DA2342352","FS4235363")
print(type(panCards))

print(panCards)



#SET

colors ={"red","blue","green","red","yello","blue"}
print(colors)

votes =["a","b","a","c","a","a","b","a","c"]

print(len(votes))
print("set voters",set(votes))