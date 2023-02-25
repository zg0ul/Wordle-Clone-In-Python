letters = 5

def LoadWords():
    '''
    Loads the words_alpha file which contains words with no numbers or letters, 
    then selects only the words that are 5 letter long for the game.
    '''
    
    with open('Dataset/words_alpha.txt') as word_file:
        valid_words = list(word_file.read().split())
        
        words = list() #creates an empty set of all the alowed words
        
        for word in valid_words:
            if len(word) == letters:
                words.append(word)
                
    return words