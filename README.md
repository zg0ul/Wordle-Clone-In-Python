<img src="https://user-images.githubusercontent.com/79023856/224111116-37bda7e7-d408-4698-b30b-bd286e19b193.png" align="left" width="70" height="70">

# Wordle Clone in Python

## Description


### What is Wordle?

Wordle is a web-based word game created and developed by Welsh software egineer Josh wardle and owned and published by the New York Times Company since 2022.  
Every day, a five-letter word is chosen at random wich players aim to guess within six tries. After every guess, each letter is marked as either green, yellow or gray: green indicates that letter is correct and in the correct position, yellow means it is in the answer but not in the right position, while gray indicates it is not in the answer at all.[^1]  


<img src="https://user-images.githubusercontent.com/79023856/221371381-624402bd-f5a7-4c87-9764-fc05bed45f26.png" width="500">

---

### Why PyQt5?

PyQt5 is a Python binding of the popular GUI (Graphical User Interface) toolkit, Qt. It allows developers to create desktop applications that can run on different operating systems, such as Windows, macOS, and Linux. PyQt5 provides a wide range of features and widgets for building interactive and professional-looking applications.

In addition, PyQt5 includes a designer called "QT Designer" that enables developers to create beautiful GUIs that can be programmed to perform various tasks.

PyQt5 has a wide range of uses. It can be used to develop games, desktop applications, educational apps, and scientific computing and data visualization using Python libraries such as NumPy, Pandas, and Matplotlib, which are important for data science. The main purpose of the **Wordle Clone** was to practice PyQt5 and gain more familiarity with its capabilities.

---

### Files and Folders

<code>***Assets***</code> folder contains the *Icons* folder as well as all the UI files generated by QT Designer.  
<code>***Dataset***</code> folder contains the words data used for the game in `words_alpha.txt`.  
<code>***Fonts***</code> folder contains the fonts used in the clone.  
<code>***Logs***</code> folder is initially empty and is used to track if the player won or lost in a given day, and they can't play more than once.  

---

### Usage & Info

To use this program, simply run the <code>**main.py**</code> file. Upon execution, the <code>main()</code> function will initialize a random word from the dataset using the current date as a seed, generating a new random word each day. An instance of the ***MainWindow*** class will then be initiated.  

The ***MainWindow*** class contains all the functionality of the game, including the main game mechanics and connections to other parts of the game in different files.

To explain how the files connect, let's start with the keyboard. There are two ways to input letters in the game: the laptop's keyboard ( <code>keyPressEvent()</code> ) and the custom-made keyboard in the game itself ( <code>ButtonClicks()</code> ). Both of these are mapped to the appropriate letter-pressed function in the <code>**keyboard.py**</code> file.

For example, if the user enters the letter "W", both of these functions will check if there is still space to add letters (i.e., if the letters in one row are less than or equal to 5, and if the number of attempts is less than or equal to 6 (maximum number of rows)). If there is space, the "W" button is connected to <code>WButtonClicked()</code>, which takes *settings.try_count* and *settings.letter_count* - global variables stored in <code>**settings.py**</code> - to indicate which row the user is filling and how many letters they have entered.

In the <code>WButtonClicked()</code> function, we first check whether there is space to insert a letter. If there is, the letter associated with the function is set for the current box to be filled, and that letter is added to a temporary string used to compare with the randomly chosen word to see if any of the letters are present in the target word. If so, we check if any of the letters are in the correct place and display that information on the game screen when the "Enter" button is pressed. This involves changing the colors of the boxes to indicate whether the letter is in the word or not. All of this is happening in the <code>BaseGame()</code> function in the <code>**main.py**</code> file.

The game is designed to be played once per day, to prevent cheating where the player can exit and re-enter the game to increase their score. To achieve this, the <code>**played_checker.py**</code> file contains three functions:
- <code>check_if_played_today()</code>: This function checks if a file with the current day's date exists in the logs folder. It is called in the *__init__* method of the **MainWindow** class in the <code>**main.py**</code> file. If the player has already played the game that day and tries to open it again, the statistics pop-up window will appear, with no option to exit. The user can only view their game stats.
- <code>add_record()</code>: This function is used in the <code>BaseGame()</code> function, and records the current date in the ***logs*** folder when the player wins or loses.
- <code>clear_logs()</code>: This function is used in the **MainWindow** loop to clear the logs, leaving only the last two. This prevents storage from running out.

Since the scores and stats were just mentioned let's talk about them, the <code>**scores.py**</code> handles just that, which has different functions:
- <code>create_file()</code>: Called in the *__init__* method of the main class to ensure that a text file called ***scores.txt*** exists, and if not, it creates it with the necessary contents, such as the number of games played, the number of wins, the current streak, the maximum streak, and the win percentage.
- <code>read_scores()</code>: Takes the file name as input (which is ***scores.txt***) and is called in the *__init__* method of the **MainWindow** class. It reads the values from the text file and assigns them to the global dictionary ***settings.Scores_dict***
- <code>update_scores()</code>: takes a boolean input whether the player won or lost (called in the <code>BaseGame()</code> function), then updates the values of ***settings.Scores_dict***.
- <code>write_scores()</code>: Called after the <code>update_scores()</code> function, takes the file name and updated scores as inputs, and then updates the text file to contain the new values.
By doing this, the app can store the user's stats and not lose them after the game is closed.

---

### Instructions for Installing Fonts

If you experience any display issues or the fonts don't appear correctly when running the game, it might be due to missing fonts on your machine. To resolve this issue, please follow the steps below:

- Navigate to the <code>Fonts</code> folder in the game directory.
- Locate the font files with the extension `.ttf` or `.otf`.
- Install the missing fonts on your machine by double-clicking on each font file and clicking the "Install" button.

After following these steps, you should be able to run the game without any issues related to missing fonts.


### Referances
[^1]: https://en.wikipedia.org/wiki/Wordle
