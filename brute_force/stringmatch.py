longstring = "I'm just a poor boy, nobody loves me"
shortstring = "loves"

def stringmatch(longstring, shortstring):
    i = 0
    while i < len(longstring):
        if longstring[i] == shortstring[0]:
            shortindex = 1
            longindex = i + 1
            while shortindex <= len(shortstring):
                if shortindex == len(shortstring):
                    return i
                if shortstring[shortindex] == longstring[longindex]:
                    shortindex = shortindex + 1
                    longindex = longindex + 1
                else:
                    break
        else:
            i = i + 1
    return -1

print(stringmatch(longstring, shortstring))
print(stringmatch(longstring, "Galileo"))
print(stringmatch(longstring, "just"))
print(stringmatch(longstring, "a poo"))
