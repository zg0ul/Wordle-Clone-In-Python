import os 
from datetime import datetime, timedelta
import settings

# Create a folder to store daily game records if it does not exist
if not os.path.exists('logs'):
    os.makedirs('logs')
    
# Get the current date
settings.today = datetime.now().date()

def check_if_played_today():
    # Check if there is a game record for today
    if os.path.exists(f'logs/{settings.today}.txt'):
        print('Sorry, you have already played today. Please come back tomorrow.')
        return True

def add_record():
    # If the player wins or loses, record the game result by creating a file with today's date
    with open(f'logs/{settings.today}.txt', 'w') as f:
        f.write(str(datetime.now()))

        

def clear_logs():  
    # Clear all game records from the designated folder at the start of each day
    yesterday = settings.today - timedelta(days=1)
    for file in os.listdir('logs'):
        file_date = datetime.strptime(file[:-4], '%Y-%m-%d').date()
        if file_date < yesterday:
            os.remove(os.path.join('logs', file))