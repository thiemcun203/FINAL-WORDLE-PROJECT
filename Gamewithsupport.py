import sys
sys.path.append('Algorithms')
ask=(input("Do you want to play in hardmode (1) or normalmode (2)?(else to stop)\n"))
while ask.isdigit():
    ASK=input('Do you want to play on our simulated game(1) or on online game(2), all with support?\n')
    while ASK.isdigit():
        if ASK=="1":
            if ask=='1':
                algo=(input('Choose algorithm to use:\n1.Random\n2.Letter Frequency\n3.Entropy\n4.Entropy + Word Frequency\nelse to change to other mode\n'))
                while algo.isdigit():
                    if algo=='1':
                        from Random.RANDOM import *
                        solution_for_simulationgame()
                    elif algo=='2':
                        from Greedy_LetterFrequency.LetterFrequency import *
                        solution_for_simulationgame()
                    elif algo=='3':
                        from Greedy_Entropy.Entropy_Hardmode import *
                        solution_for_simulationgame()
                    elif algo=='4':
                        from Greedy_Entropy_with_word_frequency.Entropy_with_word_frequency_hardmode import *
                        solution_for_simulationgame()
                    algo=(input('Choose algorithm to use:\n1.Random\n2/Letter Frequency\n3.Entropy\n4.Entropy + Word Frequency\nelse to change to other mode\n'))
            else:
                algo=input('Choose algorithm to use:\n1.Entropy\n2.Entropy + Word Frequency\nelse to change to other mode\n')
                while algo.isdigit():    
                    if algo=='1':
                        from Greedy_Entropy.Entropy_Easymode import *
                        solution_for_simulationgame()
                    elif algo=='2':
                        from Greedy_Entropy_with_word_frequency.Entropy_with_word_frequency_easymode import *
                        solution_for_simulationgame()
                    algo=input('Choose algorithm to use:\n1.Entropy\n2.Entropy + Word Frequency\nelse to change to other mode\n')
            ASK=input('Do you want to play on our simulated game(1) or on online game(2), all with support?\n')

        else:
            print(f'Access the real game with by the link https://www.nytimes.com/games/wordle/index.html or https://wordleplay.com')
            if ask=='1':
                algo=(input('Choose algorithm to use:\n1.Random\n2.Letter Frequency\n3.Entropy\n4.Entropy + Word Frequency\nelse to change to other mode\n'))
                while algo.isdigit():
                    if algo=='1':
                        from Random.RANDOM import *
                        solution_for_realgame()
                    elif algo=='2':
                        from Greedy_LetterFrequency.LetterFrequency import *
                        solution_for_realgame()
                        
                    elif algo=='3':
                        from Greedy_Entropy.Entropy_Hardmode import *
                        solution_for_realgame()
                        
                    elif algo=='4':
                        from Greedy_Entropy_with_word_frequency.Entropy_with_word_frequency_hardmode import *
                        solution_for_realgame()
                        
                    algo=(input('Choose algorithm to use:\n1.Random\n2/Letter Frequency\n3.Entropy\n4.Entropy + Word Frequency\nelse to change to other mode\n'))
            
            else:
                algo=input('Choose algorithm to use:\n1.Entropy\n2.Entropy + Word Frequency\nelse to change to other mode\n')
                while algo.isdigit():    
                    if algo=='1':
                        from Greedy_Entropy.Entropy_Easymode import *
                        solution_for_realgame()
                        
                    elif algo=='2':
                        from Greedy_Entropy_with_word_frequency.Entropy_with_word_frequency_easymode import *
                        solution_for_realgame()
                        
                    algo=input('Choose algorithm to use:\n1.Entropy\n2.Entropy + Word Frequency\nelse to change to other mode\n')
            ASK=input('Do you want to play on our simulated game(1) or on online game(2), all with support?\n')
    ask=(input("Do you want to play in hardmode (1) or normalmode (2)?(else to stop)\n"))

