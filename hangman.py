#Hangman.py

word = 'hang'
no_attempt = 6

print ("The word has " + str(len(word)) + " letters and you have 6 guesses. \nLet's Play")

l = list(word)
good_guess = []
bad_guess = []

def call_print():
    print ("Good Guess so far: " + str(good_guess))        
    print ("Bad guesses: "+ str(bad_guess))
    print ("No. of attempts left: "+ str(no_attempt))
    print ("No. of letters left: "+ str(len(l)))


while (no_attempt > 0):
    x = input ("Make a guess: ")

    if x in good_guess or x in bad_guess:
        print ("This letter was tried earlier. Make another guess.")

    else:
        if x not in l:
            print ("Wrong Guess !")
            no_attempt-=1
            bad_guess.append(x)

        else:
            print ("Good Guess ! ")
            good_guess.append(x)
            l.remove(x)

        call_print()
    
        if len(l) == 0:
            print ("YOU WIN")
            break
        elif len(l) != 0 and no_attempt == 0:
            print ("Sorry, you LOOSE")