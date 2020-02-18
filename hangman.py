"""
Coursework Assignment 2
CSC061
2019/20
"""

import time
from random import randint


class Game:
    """
    'Game' class stores variables for wins, losses, strikes,
    previous guesses etc along with the functions needed to play the game.
    """

    def __init__(self):
        self.strikes = 0
        self.playerWins = 0
        self.playerLosses = 0
        self.computerWins = 0
        self.computerLosses = 0
        self.guesses = []
        self.wrong = 0
        self.rounds = 0

        # Dictionary used to store different parts of hangman ASCII, the key is
        # associated with the number of incorrect guesses.
        self.hangDict = {
            0: "\n",

            1: "\n" * 42
               + """                         
          `        ^*+)-.:v.^^` 
          ^=+*|*+)====}^-----,` 
            """,

            2: """
               
                             
                           r-   
                           I-   
                           t_   
                           i.   
                           l`   
                           V`   
                          `T,   
                           t    
                           t    
                          `I    
                          `r    
                          `l    
                          .l    
                          ~r    
                          -t    
                          -r    
                          :l    
                          :i    
                          --    
                          l:    
                          r-    
                          t-    
                          r~    
                          l.    
                          l'    
                          }`    
                          j`    
                          t     
                          t     
                          t     
                         `t     
                         `l     
                         'l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
          `        ^*+)-.:v.^^` 
          ^=+*|*+)====}^-----,`""",

            3: """   
     :=cI@*-,_^^'`\\u,^^^^~_u:   
                           r-   
                           I-   
                           t_   
                           i.   
                           l`   
                           V`   
                          `T,   
                           t    
                           t    
                          `I    
                          `r    
                          `l    
                          .l    
                          ~r    
                          -t    
                          -r    
                          :l    
                          :i    
                          --    
                          l:    
                          r-    
                          t-    
                          r~    
                          l.    
                          l'    
                          }`    
                          j`    
                          t     
                          t     
                          t     
                         `t     
                         `l     
                         'l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
          `        ^*+)-.:v.^^` 
          ^=+*|*+)====}^-----,`""",

            4: """
     :=cI@*-,_^^'`\\u,^^^^~_u:   
                   ,v.     r-   
                    `?/    I-   
                      /i   t_   
                       :)  i.   
                        _I^l`   
                         .vV`                          
                          `T,   
                           t    
                           t    
                          `I    
                          `r    
                          `l    
                          .l    
                          ~r    
                          -t    
                          -r    
                          :l    
                          :i    
                          --    
                          l:    
                          r-    
                          t-    
                          r~    
                          l.    
                          l'    
                          }`    
                          j`    
                          t     
                          t     
                          t     
                         `t     
                         `l     
                         'l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
          `        ^*+)-.:v.^^` 
          ^=+*|*+)====}^-----,`""",

            5: """
     :=cI@*-,_^^'`\\u,^^^^~_u:   
        'l         ,v.     r-   
        .l          `?/    I-   
        .l            /i   t_   
        ^r             :)  i.   
        -v              _I^l`   
        -t               .vV`   
        -r                `T,       
                           t    
                           t    
                          `I    
                          `r    
                          `l    
                          .l    
                          ~r    
                          -t    
                          -r    
                          :l    
                          :i    
                          --    
                          l:    
                          r-    
                          t-    
                          r~    
                          l.    
                          l'    
                          }`    
                          j`    
                          t     
                          t     
                          t     
                         `t     
                         `l     
                         'l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
          `        ^*+)-.:v.^^` 
          ^=+*|*+)====}^-----,`""",

            6:"""
    :=cI@*-,_^^'`\\u,^^^^~_u:   
        'l         ,v.     r-   
        .l          `?/    I-   
        .l            /i   t_   
        ^r             :)  i.   
        -v              _I^l`   
        -t               .vV`   
        -r                `T,   
        -}                 t    
   `71+}:jil               t    
   l:       di            `I    
  '}  X   X  Dd^          `r    
   i/        MX           `l    
   `|>+7oT-t /            .l    
        tl`7;             ~r    
       ,;t`~r             -t    
       ?'t  t             -r    
      `j^r  r^            :l    
      ;]:l  1:            :i    
      t~;)  :]            --    
      : *;  '+            l:    
        i+                r-    
        n}                t-    
        &v                r~    
        }t`               l.    
        r}-               l'    
        l;>               }`    
        }`v`              j`    
        v`)*              t     
        +*`v`             t     
         I`;7             t     
         *+ j`           `t     
         `v +*           `l     
         /= l-           'l     
         :` ,            .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
                         .l     
          `        ^*+)-.:v.^^` 
          ^=+*|*+)====}^-----,`"""
    }

    def guess(self):
        """
        Random number generated and converted into an ASCII character.
        If it has already been guessed then another random integer is generated.
        """
        validGuess = False

        while validGuess == False:
            guess = chr(randint(65, 90))
            if guess not in self.guesses:
                validGuess = True
        self.guesses.append(guess)

        return guess

    def drawing(self):
        """
        Returns relevant hangman drawing, depending on how many wrong
        guesses there have been.
        """
        return self.hangDict.get(self.wrong)

    def inputValidation(self, prompt, type, validList):
        """
        Takes three arguments:

        --prompt (The string displayed when asking for input)
        --type (The type of input expected)
        --validList (A list or range object containing all valid inputs)

        Loops until input is valid and returns input.
        """
        valid = False

        if type == "str":
            while not valid:
                userInput = str(input(prompt)).upper()
                if userInput not in validList:
                    print("Invalid input. Try again.")
                    continue
                else:
                    output = userInput
                    valid = True

        elif type == "int":
            while not valid:
                try:
                    userInput = int(input(prompt))
                except ValueError:
                    print("Invalid input. Try again.")
                    continue
                if userInput not in validList:
                    print("Input not in range. Try again.")
                    continue
                else:
                    output = userInput
                    valid = True

        return output

    def playRound(self):
        """
        Begins the next round, takes input and runs until 6 incorrect guesses
        have been made or until all the letters in the word have been guessed.
        """
        print(
            "This is round {}\n"
            "Your word must be between 5 and 10 letters long, "
            "and cannot contain numbers.\n\n"
            "Computer: {} Wins  {} Losses\n"
            "You:  {} Wins  {} Losses\n\n"
            "How many letters are there in your word?\n"
            .format(
                self.rounds, self.computerWins, self.computerLosses,
                self.playerWins, self.playerLosses
            )
        )

        userInput = self.inputValidation(
            "Please enter a whole number:\n",
            "int", range(5, 11)
        )

        print("Let's begin. Your word has {} letters".format(userInput))

        wordLen = userInput
        remainingLen = userInput
        string = "_ " * wordLen
        indexList = [] # Stores indexes of successfully guessed letters

        while self.wrong < 6 and remainingLen > 0:
            print("\n"*200)
            print(self.drawing())
            print("Incorrect guesses: {}".format(self.wrong))
            print(string + "\n\n")

            currentGuess = self.guess()
            userInput = self.inputValidation(
                "Is the letter {} in your word?"
                "\nY/N\n".format(currentGuess),
                "str", ["Y", "N"]
            )

            if userInput == "N":
                self.wrong += 1


            elif userInput == "Y":
                loop = True
                while loop:
                    n = self.inputValidation(
                        "How many times does the letter {} "
                        "occur in your word?\n".format(currentGuess),
                        "int",
                        range(1, remainingLen + 1)
                        )
                    i = 1
                    while i <= wordLen and n > 0:
                        if i in indexList:
                            i += 1
                        else:
                            userInput = self.inputValidation(
                                "Is it letter number {}?\nY/N\n".format(i),
                                "str",
                                ["Y", "N"]
                            )
                            if userInput == "Y":
                                indexList.append(i)
                                string = list(string)
                                string[i * 2 - 2] = currentGuess
                                string = "".join(string)
                                remainingLen -= 1
                                n -= 1
                                i += 1
                                loop = False
                            elif userInput == "N":
                                i += 1

                    # Penalises player for deception.
                    if loop:
                        self.strikes += 1
                        if self.strikes < 3:
                            print(
                                "Thought you could pull a fast one on me?\n"
                                "This is Strike {}, {} more and you forfeit "
                                "this round"
                                .format(self.strikes, 3-self.strikes)
                            )
                        else:
                            print("That was your last chance.")
                            remainingLen = 0
                            loop = False
                            time.sleep(5)

        if remainingLen <= 0:
            self.computerWins += 1
            self.playerLosses += 1
            print(self.drawing())
            print("\nThe Computer has won this round!\n")

        if self.wrong >= 6:
            self.playerWins += 1
            self.computerLosses += 1
            print(self.drawing())
            print("\nYou have won this round!\n")

        if self.rounds < 6:
            # Calls nextRound method if less than 6 rounds have been played.
            # This is how the game constantly progresses through rounds until
            # specific criteria are met.
            self.nextRound()

    def nextRound(self):
        """
        Clears scores and lists for next round, if there have been less than 5
        rounds in total, and less than 3 wins, then starts next round.

        Otherwise the next round is not initiated, and the program can
        terminate in main()
        """
        if self.rounds < 5 and self.computerWins < 3 and self.playerWins < 3:
            self.wrong = 0
            self.guesses = []
            self.rounds += 1
            self.strikes = 0
            self.playRound()

        else:
            if self.computerWins > self.playerWins:
                print("Computer wins!")
            elif self.playerWins > self.computerWins:
                print("Congratulations, you won against "
                      "a randomn number generator!")


def main():
    """
    Initialises Game class, calls nextRound function, then prints the
    intro and final scores. Calling the first nextRound function initiates
    the progression through each round, because the nextRound and playRound
    functions both call each other if certain criteria are met.
    """
    print("\nWelcome to Hangman! The educational spelling game "
          "based on an outdated method of execution!\n\n")

    game = Game()
    game.nextRound()

    print(
        "\nFinal Scores!\n\n"
        "Computer: {} Wins  {} Losses\n"
        "You:  {} Wins  {} Losses\n"
        .format(
            game.computerWins, game.computerLosses,
            game.playerWins, game.playerLosses
        )
    )


main()