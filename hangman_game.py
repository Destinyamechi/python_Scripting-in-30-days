def hangman(word, num_of_players):
    word_list = [a for a in word]
    score_list = [0 for x in range(num_of_players)]
    player_list = [x for x in range(num_of_players)]
    player = 0
    
    while len(word_list) != 0: # as long as the wordcount of the word_list is geater than 0

        if player == num_of_players: # assigning each game to a different player
            player = 0
        guess = input("Enter a guess: ")
        if guess in word_list:
            print('Correct guess')
            word_list.remove(guess) # removing the guessed word from the list 
            score_list[player] += 1 # adding to the score of the player
        else:
            print('Wrong guess or the word\'s already taken')
        player += 1 # changing players
         

    score = dict(zip(player_list, score_list)) # returning results in a zipped dictionarry format of 2 lists
    return score

word = input("Enter the word: ")
num_of_players = int(input("Enter the number of players: "))
print(hangman(word, num_of_players))