def censor(text, word):
    textlist = text.split()
    for i in range(len(textlist)):
        if textlist[i] == word:
            textlist[i] = '*' * len(word)
            
    return " ".join(textlist)
