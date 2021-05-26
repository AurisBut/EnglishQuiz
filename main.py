import random
# import pyttsx3
# engine = pyttsx3.init()


with open('lithuanian-words-list.txt', 'r', encoding='utf-8') as file:
    allText = file.read()
    words = list(map(str, allText.split('\n')))
    rword = random.choice(words)
    print(rword)


answer = input("Play game? ('y' to continue) ").lower()
print(" ")
while answer == "y":

    vocabDictionary = {
        'labas': 'hello',
        'mergaitė': 'girl',
        'berniukas': 'boy',
        'rytoj': 'tomorrow',
        'vakar': 'yesterday',
        'Lietuva': 'Lithuania',
        'darbas': 'work',
        'mėnulis': 'moon',
        'kompiuteris': 'computer',
        'pagalvė': 'pillow',
        'užuolaida': 'curtain',
        'langas': 'window',
        'durys': 'door',
        'virtuvė': 'kitchen',
        'pusryčiai': 'breakfast',
        'klaviatūra': 'keyboard',
        'pusbloris': 'cousin',
        'žemė': 'earth',
        'triušis': 'rabbit',
        'nežinomas': 'unknown',
        'kareivis': 'soldier',
        'kariuomenė': 'army',
        'kuprinė': 'backpack',
        'genys': 'woodpecker',
        'lapas': 'leaf',
        'ateitis': 'future',
        'kinas': 'cinema',
        'piktas': 'angry',
        'dangus': 'sky',
        'požemis': 'underground',
        'nuotolinis': 'remote',
        'tarakonas': 'cockroach',
        'grūdas': 'grain',
        'agurkas': 'cucumber',
        'pomidoras': 'tomato',
        'krepšinis': 'basketball',
        'nuotykis': 'adventure',
        'sostinė': 'capital',
        'šalis': 'country',
        'sveikas': 'healthy',
        'paplūdimys': 'beach',


    }

    keyword_list = list(vocabDictionary.keys())  # turns words into a list
    random.shuffle(keyword_list)  # shuffle keywords

    correct = 0
    wrong = 0

    for keyword in keyword_list:
        display = "{}"
        print(display.format(keyword))
        engine.say(f"{vocabDictionary[keyword]}")
        engine.runAndWait()
        userInputAnswer = input("ANSWER: ")
        print(vocabDictionary[keyword])

        print(" ")
        if userInputAnswer == (vocabDictionary[keyword]):
            print("CORRECT")
            correct += 1
            engine.say('CORRECT')
            engine.runAndWait()
        else:
            print(f"WRONG, correct answer is --> {(vocabDictionary[keyword])} <--")
            wrong += 1
            engine.say('WRONG')
            engine.runAndWait()

        print('_' * 25)  # line separator

    display = "SCORE: {} correct and {} wrong"
    print(" ")
    print(display.format(correct, wrong))
    engine.say(f'NICE JOB! You answered correctly {correct} and failed {wrong} times.')
    engine.runAndWait()
    answer = input("Play again? ('y' to continue) ")

print(" ")
print("Thanks for playing")
