import sys
sys.path.append('Algorithms')
ask=(input("Do you want to play in hardmode (1) or normalmode (2)?(else to stop)\n"))
while ask.isdigit():
    if ask=='1':
        algo=(input('Choose algorithm to use:\n1.Random\n2.Letter Frequency\n3.Entropy\n4.Entropy + Word Frequency\nelse to change to other mode\n'))
        while algo.isdigit():
            if algo=='1':
                from Random.RANDOM import *
                solution_for_WordleBot()
            elif algo=='2':
                from Greedy_LetterFrequency.LetterFrequency import *
                solution_for_WordleBot()
            elif algo=='3':
                from Greedy_Entropy.Entropy_Hardmode import *
                solution_for_WordleBot()
            elif algo=='4':
                from Greedy_Entropy_with_word_frequency.Entropy_with_word_frequency_hardmode import *
                solution_for_WordleBot()
            algo=(input('Choose algorithm to use:\n1.Random\n2/Letter Frequency\n3.Entropy\n4.Entropy + Word Frequency\nelse to change to other mode\n'))
    else:
        algo=input('Choose algorithm to use:\n1.Entropy\n2.Entropy + Word Frequency\nelse to change to other mode\n')
        while algo.isdigit():    
            if algo=='1':
                from Greedy_Entropy.Entropy_Easymode import *
                solution_for_WordleBot()
            elif algo=='2':
                from Greedy_Entropy_with_word_frequency.Entropy_with_word_frequency_easymode import *
                solution_for_WordleBot()
            algo=(input('Choose algorithm to use:\n1.Random\n2/Letter Frequency\n3.Entropy\n4.Entropy + Word Frequency\nelse to change to other mode\n'))
    ask=(input("Do you want to play in hardmode (1) or normalmode (2)?(else to stop)\n"))

