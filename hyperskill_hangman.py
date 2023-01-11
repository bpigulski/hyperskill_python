print("H A N G M A N")
print('')
import random
guess = ''
words = ['python', 'java', 'swift', 'javascript']
gap = '-'
i = 8
v_won = 0
v_lost = 0
menu = 0
while menu == 0:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    menu_ans = input()
    if menu_ans == 'exit':
        menu = 1
    if menu_ans == 'results':
        print('You won: {} times.'.format(v_won))
        print('You lost: {} times.'.format(v_lost))
    if menu_ans == 'play':
        i = 0
        random.shuffle(words)
        answ = words[0]
        answ_list = list(answ)
        answ_tmp = list(gap * len(answ))
        tried_ltrs = []
    while i < 8 :
        print(''.join(answ_tmp))
        print("Input a letter:")
        letter = input()
        if len(letter) != 1:
            print('Please, input a single letter.')
        elif (letter.islower() is True) and (letter.isalpha() is True):
            if letter in list(tried_ltrs):
                print("You've already guessed this letter.")
            if letter in answ_list:
                for j in range(0, len(answ_list)):
                    if answ_list[j] == letter:
                        answ_tmp[j] = str(letter)
            else:
                print("That letter doesn't appear in the word")
                i = i + 1
                if i == 8:
                    print('You lost!')
                    v_lost = v_lost + 1
            if answ_list == answ_tmp:
                print('You guessed the word {}!'.format(answ))
                print('You survived!')
                v_won = v_won + 1
                i = 8
            tried_ltrs.append(letter)
        elif (letter.islower() is False) or (letter.isalpha() is False):
            print('Please, enter a lowercase letter from the English alphabet.')
        print('')

