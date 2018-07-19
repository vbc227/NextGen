from random import choice

correct_guess= ()
words=('dog', 'bird', 'truck')
random_word= choice(words)
for x in random_word:
    print('_', end='')
while len(correct_guess)!= len(random_word):
    user_guess=input('Guess a letter here')
    if user_guess in random_word:
        print('good guess')
        correct_guess= correct_guess+ (user_guess,)
    else:
        print('try again')
    for w in random_word:
        if w in correct_guess:
            print (w,end='')
        else:
            print('_', end='')
print('Done with Game')