#Pedro Galllino
#10/20/17
#stringUnion.py - unites two strings

def stringUnion(word1, word2):
    total = " "
    for ch in word1:
        if not ch in total:
            total += ch
            
    for ch in word2:
        if not ch in total:
            total += ch
    
    return total

print(stringUnion("mississippi", "pennsylvania"))
    
