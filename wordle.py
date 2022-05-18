from english_words import english_words_set
from collections import Counter
import sys

### Listing all 5 letter words in the english language
five_letter_words0 = []
for word in english_words_set:
    word = word.replace("'","")
    word = word.replace(".","")
    word = word.replace("'","")
    if len(word)==5:
        word = word.lower()
        five_letter_words0.append(word)


print("Available Words:",len(five_letter_words0))

frequency = {'e':11.1607,
            'm':3.0129,
            'a':8.4966,
            'h':3.0034,
            'r':7.5809,
            'g':2.4705,
            'i':7.5448,
            'b':2.0720,
            'o':7.1635,
            'f':1.8121,
            't':6.9509,
            'y':1.7779,
            'n':6.6544,
            'w':1.2899,
            's':5.7351,
            'k':1.1016,
            'l':5.4893,
            'v':1.0074,
            'c':4.5388,
            'x':0.2902,
            'u':3.6308,
            'z':0.2722,
            'd':3.3844,
            'j':0.1965,
            'p':3.1671,
            'q':0.1962}

options = {}
for word in five_letter_words0:
    score = 0
    for i,letter in enumerate(word):
        if letter not in word[:i]:
            score += frequency[letter]
    options[word] = score
sorted_options = {k: v for k, v in sorted(options.items(), key=lambda item: item[1],reverse = True)}

### Running the user through their guesses and results and suggesting the next guess
for guess_number in range(6):

    while True:
        print()
        guess1 = input(f"Guess Number {guess_number+1} (e.g. adieu) (type exit to exit): ")
        if guess1 == 'exit':
            sys.exit()
        if len(guess1) == 5:
            break
    
    while True:
        result1 = input("Colors for Guess (e.g. xgyxx (x=gray, g=green, y=yellow)): ")
        outcome = True
        for letter in result1:
            if letter not in ['x','y','g']:
                outcome = False
        if len(result1) == 5 and outcome == True:
            break
    

    remove = []
    for i, letter in enumerate(guess1):
        if result1[i] == 'g':
            for j, word in enumerate(sorted_options.keys()):
                if word[i] != letter:
                    remove.append(word)
                    result = word in sorted_options.keys()
        elif result1[i] == 'x':
            for j, word in enumerate(sorted_options.keys()):
                if Counter(word)[letter] >= Counter(guess1)[letter]:
                    remove.append(word)
                    result = word in sorted_options.keys()
        elif result1[i] == 'y':
            for j, word in enumerate(sorted_options.keys()):
                if letter not in word or letter == word[i]:
                    remove.append(word)
    for word in remove:
        if word in sorted_options.keys():
            del sorted_options[word]
    print()
    print("Available Words:",len(sorted_options.keys()))
    if len(sorted_options.keys()) > 1:
        print()
        print(f'Choose a word from this list')
        print(list(sorted_options.keys()))
        print(f'Best Guess: {list(sorted_options.keys())[0]}')
    if len(sorted_options.keys()) == 1:
        print()
        for key, value, in sorted_options.items():
            print(f'Yay! The answer should be {key}')
        
        sys.exit()
    if len(sorted_options.keys()) == 0:
        print('Oops I missed something. No more words to try. Try again.')