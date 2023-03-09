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

Now, the game works well when the player is allowed to play once per day, otherwise they can figure out the word then keep exiting and entering the game each time increasing the score which is cheating, to take care of that, <code>**played_cheker.py**</code> file, which contains 3 functions, <code>check_if_played_today()</code>: checks if there is a file with the current day's date as a name in the ***logs*** folder, it is called in the init method of the MainWindow Class in the main.py file, if the player already played today and tries to open the game, the statistics pop up window appears with no way to exit it, all the user can do is look at how many games they played, how many won, etc.
<code>add_record()</code>: used in the <code>BaseGame()</code> when the player wins or loses the function add a record of today's date in the ***logs*** folder.
<code>clear_logs()</code>: used in the MainWindow loop to clear the logs leaving the last two, to prevent storage run out.

### Referances
[^1]: https://en.wikipedia.org/wiki/Wordle
