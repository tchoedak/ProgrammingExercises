def reverse(text):
    revtext = []
    for i in range(len(text)):
        revtext.append(text[-i -1])
    combtext = ''
    return combtext.join(revtext)
