text = input()

def count_letters(text):
    vowels = 'уеёыаоэяиюУЕЁЫАОЭЯИЮ'
    consonants = 'йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ'

    vowels_count = 0
    consonants_count = 0

    for letter in text:
        if letter in vowels:
            vowels_count += 1
        elif letter in consonants:
            consonants_count += 1
    print(f'Гласных: {vowels_count}, Согласных: {consonants_count}')

count_letters(text)
