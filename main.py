import random
import sys

class Game:
    b = ['python', 'java', 'kotlin', 'javascript']
    c = random.choice(b)
    d = list(c)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def game(self):
        show = "-" * (len(self.c))
        show1 = list(show)
        show2 = "".join(show1)
        count = 0
        letters = []
        while count < 8:
            print("")
            print(show2)
            guess = input("Input a letter:")
            if len(guess) > 1:
                print("You should input a single letter")
                print("")
            elif guess not in self.alphabet:
                print("Please enter a lowercase English letter")
                print("")
            elif guess in self.c:
                if guess in show2:
                    print("You've already guessed this letter")
                    print("")
                else:
                    p1 = [i for i, j in enumerate(self.d) if j == guess]
                    for i in range(len(p1)):
                        show1[p1[i]] = guess
                        show2 = "".join(show1)
                        letters.append(guess)
                    print("")
                    if show2 == self.c:
                        print(show2)
                        print("You guessed the word!\nYou survived!")
                        Game.choice(self)
            elif guess in letters:
                print("You've already guessed this letter")
                print("")
            else:
                print("That letter doesn't appear in the word")
                letters.append(guess)
                count += 1
        else:
            print("You lost!")

    def choice(self):
        answer = input('Type "play" to play the game, "exit" to quit:')
        if answer == "play":
            self.game()
        else:
            sys.exit()

print("H A N G M A N")
nowa_gra = Game()
nowa_gra.choice()
