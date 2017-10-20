#Pedro Galllino
#10/20/17
#stringUnion.py - unites two strings

total = ''
def stringUnion(word1,word2):
    for ch in word1:
        if ch not in total:
            total = str(total)+str(ch)
    for ch in word2:
        if ch not in total:
            total = str(total)+str(ch)

stringUnion('big','bro')
    
