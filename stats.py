def num_of_words(text):
    return(len(text.split()))

def num_of_characters(noc):
    dic = {}
    char = noc.lower()
    for character in char:
        if character in dic:
           dic[character]+=1
        if character not in dic:
            dic[character] = 1
    return dic
    