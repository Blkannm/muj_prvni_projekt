"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Trung Le
email: trung.le3301@gmail.com
discord: BLKANNM#1363
"""


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user_and_pass = {
    'bob' : '123',
    'ann' : 'pass123',
    'mike' : 'password123',
    'liz' : 'pass123'
}
slicer = "="*50
name = input('name: ')
password = input('password: ')
print(slicer)
if name in user_and_pass and user_and_pass[name] == password:
    print(f'Welcome {name}.')
    print("We have 3 texts to be analyzed.")
    print(slicer)

    vyber = int(input('choose number 1, 2, 3:  '))

    if vyber > 0 and vyber <= 3:
        print(slicer)
        print(TEXTS[vyber-1])
        print(slicer)

        title_words = 0
        upper_words = 0
        lower_words = 0
        numeric = 0
        summari_in_text = 0
        for word in TEXTS[vyber-1].split():
            if word[0].isupper():
                title_words += 1
            if word.isupper() and word.isalpha():
                upper_words += 1
            if word.islower():
                lower_words += 1
            if word.isnumeric():
                numeric += 1
                summari_in_text += int(word)
            
        print(f"There are {len(TEXTS[vyber-1].split())} words in the selected text.")
        print(f"There are {title_words} titlecase words.")
        print(f"There are {upper_words} uppercase words.")
        print(f"There are {lower_words} lowercase words.")
        print(f"There are {numeric} numeric strings.")
        print(f"The sum of all the numbers {summari_in_text}")
        print(slicer)

        print("LEN|  OCCURENCES  |NR.")
        print(slicer)
        

        #tabulka delek slov
        rozdelena_slova: list() = TEXTS[vyber-1].split()
        delka_slov:dict = dict()
        for each_words in rozdelena_slova:
            len_of_words = len(each_words)
            if len_of_words not in delka_slov:
                delka_slov[len_of_words] = 1
            else:
                delka_slov[len_of_words] += 1

        for zkouska in sorted(delka_slov.keys()):
            print(f"{zkouska:2}.|{'*'*delka_slov[zkouska]: <12}|{delka_slov[zkouska]: 2}")

    else :
        print('invalid input!')

else:
    print("Password or username aren't in database.")