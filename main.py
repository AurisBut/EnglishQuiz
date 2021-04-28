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
        'Lietuva': 'lithuania',
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
        else:
            print("WRONG")
            wrong += 1

        print('_' * 25)  # line separator

    display = "SCORE: {} correct and {} wrong"
    print(" ")
    print(display.format(correct, wrong))
    answer = input("Play again? ('y' to continue) ")

print(" ")
print("Thanks for playing")
