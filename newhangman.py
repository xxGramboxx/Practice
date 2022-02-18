def hangman():
    word_bank = ['yes', 'no', 'hello', 'jason', 'nick']
    print("let's play hangman.  you have 10 guesses to get the word right.  type only 1 letter at a time.")
    import random
    secret_word = random.choice(word_bank)
    x = []
    for i in secret_word:
        x.append('_')
    print(" ".join(x))
    def guesss():
        guess = input('GUESS: ')
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                x[i] = guess
    guesses_left = 10
    while guesses_left != 0:
        if ''.join(x) != secret_word:
            print(f"you have {guesses_left} guess(es) remaining")
            guesss()
            print(' '.join(x))
            guesses_left -= 1
        else:
            print('you win!')
            break
    if guesses_left == 0:
        print('you lose')
hangman()
y = input('play again? ')
while y == 'yes' or y == 'y':
    hangman()
    y = input('play again? ')
print('thanks for playing...goodbye!')
h ="  O"
a ="  |"
n ="/ | \\"
g =" / \\"
print(h)
print(a)
print(n)
print(g)