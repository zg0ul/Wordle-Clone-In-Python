from load_words import LoadWords

def init():
    global letter_count
    letter_count = 0
    
    global max_letter_count
    max_letter_count = 5
    
    global try_count
    try_count = 0
    
    global max_try_count
    max_try_count = 6
    
    global words
    words = LoadWords() # Loads the words that can be used
    
    global wordchoice
    
    global tempstring
    tempstring = ""
    
    global boxes
    
    global FilledBox
    FilledBox = """
                    color: white;
                    border:2px solid rgb(96, 97, 98);

        """
        
    global DefaultBox
    DefaultBox = """
                color: white;
                border:2px solid rgb(58, 58, 60);
    """
        
    global wrongLetterBox
    wrongLetterBox = """
                        color: white;
                        border:2px solid rgb(58, 58, 60);
                        background-color: rgb(58, 58, 60);
    """
    
    global rightLetterBox
    rightLetterBox = """
                        color: white;
                        background-color: rgb(83, 141, 78);

    """
    
    global semirightLetterBox
    semirightLetterBox = """
                            color: white;
                            background-color: rgb(181, 159, 59)
    """
    
    global defaultButton
    defaultButton = """
                    background-color:rgb(129, 131, 132);
                    font: 75 14pt "Clear Sans";
                    color:white;
                    border-radius:7px;
    """
    
    global wrongButton
    wrongButton = """
                    background-color:rgb(58, 58, 60);
                    font: 75 14pt "Clear Sans";
                    color:white;
                    border-radius:7px;
    """
    
    global semirightButton
    semirightButton = """
                        background-color:rgb(181, 159, 59);
                        font: 75 14pt "Clear Sans";
                        color:white;
                        border-radius:7px;
    """
    
    global rightButton
    rightButton = """
                    background-color:rgb(83, 141, 78);
                    font: 75 14pt "Clear Sans";
                    color:white;
                    border-radius:7px;
    """
    
    global Buttons
    Buttons = {}
    
    global ScoresButtonStyle
    ScoresButtonStyle = '''
                            QPushButton{background:transparent;
                                    backgorund:none;
                                    background-repeat:none;
                                    border-image:url("Assets/Icons/podium_white.png");}
                            '''
                            
    global HowToButtonStyle
    HowToButtonStyle = '''
                            QPushButton{background:transparent;
                                    backgorund:none;
                                    background-repeat:none;
                                    border-image:url("Assets/Icons/question-mark.png");}
                            '''
                            
    global NumOfPlayed_new
    
    global Number_of_games_played
    
    global Win_Percentage
    
    global Current_streak
    
    global Max_streak
    
    global Number_of_wins
    
    global Scores_dict
    Scores_dict = dict()
    
    global file_name
    
    global contents
    
    global today
    
    global check
    
    global WonLost
    WonLost = False
    
    
init()