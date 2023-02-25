import settings
import os

settings.file_name = "scores.txt"
settings.contents = """Number_of_games_played: 0
Number_of_wins: 0
Current_streak: 0
Max_streak: 0
Win_Percentage: 0"""

def create_file():
    # Checks if the file exists
    if not os.path.exists(settings.file_name):
        # If the file doesn't exist, create it and write the contents
        with open(settings.file_name, "w") as f:
            f.write(settings.contents)
            
def read_scores(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    print(lines)
    
    for line in lines:
        key, value = line.strip().split(': ')
        settings.Scores_dict[key] = int(value)
    return settings.Scores_dict

def write_scores(filename, scores):
    with open(filename, 'w') as f:
        for key, value in scores.items():
            f.write('{}: {}\n'.format(key, value))

def update_scores(win:bool):
    settings.Scores_dict["Number_of_games_played"] += 1
    settings.Scores_dict["Win_Percentage"] = int((settings.Scores_dict['Number_of_wins'] / settings.Scores_dict["Number_of_games_played"] * 100))
    if not win:
        settings.Scores_dict["Current_streak"] = 0
    else:
        settings.Scores_dict['Number_of_wins'] = settings.Scores_dict['Number_of_wins'] + 1
        settings.Scores_dict["Current_streak"] = settings.Scores_dict["Current_streak"] + 1
        
    settings.Scores_dict['Max_streak'] = max(settings.Scores_dict['Max_streak'], settings.Scores_dict["Current_streak"])
    settings.Scores_dict.update({
        'Number_of_games_played': int(settings.Scores_dict["Number_of_games_played"]),
        'Number_of_wins': int(settings.Scores_dict['Number_of_wins']),
        'Win_Percentage': int(settings.Scores_dict["Win_Percentage"]),
        'Current_streak': int(settings.Scores_dict["Current_streak"]),
        'Max_streak': int(settings.Scores_dict['Max_streak']),
    })

# filename = 'scores.txt'
# scores = read_scores(filename)
# win = 1  # or 0 for a loss
# update_scores(scores)
# write_scores(filename, scores)
