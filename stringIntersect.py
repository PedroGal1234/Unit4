#Pedro Gallino
#10/23/17
#stringIntersect.py - tells you letters that apear in both words

def stringIntersect(word1, word2):
    total = " "
    for ch in word1:
        if not ch in total:
            if ch in word1 and ch in word2:
                total += ch
    return total

print(stringIntersect("mississippi", "pennsylvania"))

