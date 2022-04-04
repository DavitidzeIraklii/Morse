import pandas as pd
df = pd.read_csv('Morse.csv')

def let_to_morse():
    given_word = input('Put word here: ').lower()
    translated_list = []
    for letter in list(given_word):
        for index, row in df.iterrows():
            if letter == row['letter']:
                translated_list.append(row['morse'])
    return translated_list

def morse_to_let():
    given_word = input('Put morse here: ')
    morse_list = given_word.split()
    translated_list = []
    for letter in morse_list:
        for index, row in df.iterrows():
            if letter == row['morse']:
                translated_list.append(row['letter'])
    return translated_list


more = True
while more:
    choise = input('Letter to morse: l; morse to letter: m;\n')
    if choise == 'l':
        translated_func = let_to_morse()
        listToStr = ' '.join(map(str, translated_func))
        print(listToStr)
        more = input('One more? y/n\n')
        if more == 'y':
            more = True
        else:
            more = False
    elif choise == 'm':
        translated_func = morse_to_let()
        if translated_func == []:
            print('Wrong message!')
        else:
            listToStr = ''.join(map(str, translated_func))
            print(listToStr)
        more = input('One more? y/n\n')
        if more == 'y':
            more = True
        else:
            more = False
    else:
        print('Wrong func!')
print('Bye!')


