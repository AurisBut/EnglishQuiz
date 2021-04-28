import random
import pyttsx3
engine = pyttsx3.init()


answer = input("Play game? ('y' to continue) ").lower()
print(" ")
while answer == "y":
    with open('lithuanian-words-list.txt', 'r', encoding='utf-8') as file:
        allText = file.read()
        keyword_list = list(map(str, allText.split('\n')))
        random.shuffle(keyword_list)
        rword = random.choice(keyword_list)

        correct = 0
        wrong = 0

        for keyword in keyword_list:
            display = "{}"
            print(display.format(keyword))
            engine.say(f"{keyword}")
            engine.runAndWait()
            userInputAnswer = input("ANSWER: ")
            print(rword)

            print(" ")
            if userInputAnswer == (rword):
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
