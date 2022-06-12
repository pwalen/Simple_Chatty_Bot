text = input()

for _i in text:
    if _i in 'aeiou':
        print('vowel')
    elif _i in 'bcdfghjklmnpqrstvxzwy':
        print('consonant')
    else:
        break