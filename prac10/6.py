sentence = input()

def len_sentence(sentence):
    if len(sentence) < 160:
        return sentence
    else:
        return sentence[:160]

print(len_sentence(sentence))
