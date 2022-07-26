from english_words import english_words_lower_set as engwords
from random import randint

words = []

for word in engwords:
    if len(word) == 5:
        words.append(word)

target = words[randint(0, len(words))]
cnt = 1
print("your guesses have to be all lowercase. You have 5 tries")

while True:
    print("Try #"+str(cnt)+" — ", end="")
    guess = input("Your 5 letter word guess??")
    if cnt == 5:
        print("The word is "+target)
        print("YOU LOST!")
        break
    if target == guess:
        print("GGGGG\nCONGRATULATIONS, YOU WIN!")
        break
    for i in range(0, 5):
        if target[i] == guess[i]:
            print("G", end="")
        else:
            exist = False
            for j in range(0, 5):
                if guess[i] == target[j]:
                    exist = True
            if exist:
                print("Y", end="")
            else:
                print("N", end="")
    print("")
    cnt+=1

