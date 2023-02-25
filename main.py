import sys
import warnings
import random
import datetime
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QColor
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation, QEvent, pyqtSignal, QTimer
from pop_ups import StatisticsPopUp, HowToPopUp
import keyboard
import settings
import scores
import played_checker 

letters = 5


class MainWindow(QMainWindow):
    clicked = pyqtSignal()
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Load the Ui file
        loadUi('Assets/MainGUI.ui', self)
        
        # Set Icons and default style sheets
        self.BACKButton.setIcon(QIcon('Assets/Icons/backspace White.png'))
        self.setWindowIcon(QIcon("Assets/Wordle-Clone-Logo.png"))
        self.ScoresButton.setStyleSheet(settings.ScoresButtonStyle)
        self.HowToButton.setStyleSheet(settings.HowToButtonStyle)
        
        # Initialize pop up labels and dimmer to be hidden
        self.notwordpopup.hide()
        self.noletterspopup.hide()
        self.dimmer.hide()
        self.YouWonPopUp.hide()
        self.YouLostPopUp.hide()
        self.WordWasPopUp.hide()

        played_checker.clear_logs()
        settings.check = played_checker.check_if_played_today()
        
        if settings.check:
            self.dimmer.show()
            self.dimmer.setEnabled(False)
            self.Scores()
            
        
        # Check if the scores file exists, if not create one
        scores.create_file()
        scores.read_scores(settings.file_name)
    
    
        settings.boxes = [[self.box_1_1, self.box_1_2, self.box_1_3, self.box_1_4, self.box_1_5],
                          [self.box_2_1, self.box_2_2, self.box_2_3, self.box_2_4, self.box_2_5],
                          [self.box_3_1, self.box_3_2, self.box_3_3, self.box_3_4, self.box_3_5],
                          [self.box_4_1, self.box_4_2, self.box_4_3, self.box_4_4, self.box_4_5],
                          [self.box_5_1, self.box_5_2, self.box_5_3, self.box_5_4, self.box_5_5],
                          [self.box_6_1, self.box_6_2, self.box_6_3, self.box_6_4, self.box_6_5],]
        
        settings.Buttons = {"q": self.Test,
                            "w": self.WButton,
                            "e": self.EButton,
                            "r": self.RButton,
                            "t": self.TButton,
                            "y": self.YButton,
                            "u": self.UButton,
                            "i": self.IButton,
                            "o": self.OButton,
                            "p": self.PButton,
                            "a": self.AButton,
                            "s": self.SButton,
                            "d": self.DButton,
                            "f": self.FButton,
                            "g": self.GButton,
                            "h": self.HButton,
                            "j": self.JButton,
                            "k": self.KButton,
                            "l": self.LButton,
                            "z": self.ZButton,
                            "x": self.XButton,
                            "c": self.CButton,
                            "v": self.VButton,
                            "b": self.BButton,
                            "n": self.NButton,
                            "m": self.MButton} 
        
        if not settings.WonLost:
            self.ButtonClicks()
        
        # Show the App
        self.show() 
        
    def show_nowords_popup(self):
        self.notwordpopup.show()
        
        self.background_color = QColor(self.notwordpopup.palette().color(self.notwordpopup.backgroundRole()).rgb())
        self.fade = QPropertyAnimation(self.notwordpopup, b"windowOpacity")
        self.fade.setStartValue(1.0)
        self.fade.setEndValue(0.0)
        self.fade.setDuration(1500)
        
        self.notwordpopup.setAutoFillBackground(True)
        self.palette = self.notwordpopup.palette()
        self.palette.setColor(self.notwordpopup.backgroundRole(), Qt.transparent)
        self.notwordpopup.setPalette(self.palette)
        
        self.fade.finished.connect(self.notwordpopup.hide)
        
        self.fade.start()
    
    def show_noletters_popup(self):
        self.noletterspopup.show()
        
        self.background_color = QColor(self.noletterspopup.palette().color(self.noletterspopup.backgroundRole()).rgb())
        self.fade = QPropertyAnimation(self.noletterspopup, b"windowOpacity")
        self.fade.setStartValue(1.0)
        self.fade.setEndValue(0.0)
        self.fade.setDuration(1500)
        
        self.noletterspopup.setAutoFillBackground(True)
        self.palette = self.noletterspopup.palette()
        self.palette.setColor(self.noletterspopup.backgroundRole(), Qt.transparent)
        self.noletterspopup.setPalette(self.palette)
        
        self.fade.finished.connect(self.noletterspopup.hide)
        
        self.fade.start()
    
    def show_YouWon_popup(self):
        self.YouWonPopUp.show()
        
        self.background_color = QColor(self.YouWonPopUp.palette().color(self.YouWonPopUp.backgroundRole()).rgb())
        self.fade = QPropertyAnimation(self.YouWonPopUp, b"windowOpacity")
        self.fade.setStartValue(1.0)
        self.fade.setEndValue(0.0)
        self.fade.setDuration(10000) # shows the label for 10 seconds.
        
        self.YouWonPopUp.setAutoFillBackground(True)
        self.palette = self.YouWonPopUp.palette()
        self.palette.setColor(self.YouWonPopUp.backgroundRole(), Qt.transparent)
        self.YouWonPopUp.setPalette(self.palette)
        
        self.fade.finished.connect(self.YouWonPopUp.hide)
        
        self.fade.start()
        
    def show_YouLost_popup(self):
        self.YouLostPopUp.show()
        
        self.background_color = QColor(self.YouLostPopUp.palette().color(self.YouLostPopUp.backgroundRole()).rgb())
        self.fade = QPropertyAnimation(self.YouLostPopUp, b"windowOpacity")
        self.fade.setStartValue(1.0)
        self.fade.setEndValue(0.0)
        self.fade.setDuration(5000) # shows the label for 10 seconds.
        
        self.YouLostPopUp.setAutoFillBackground(True)
        self.palette = self.YouLostPopUp.palette()
        self.palette.setColor(self.YouLostPopUp.backgroundRole(), Qt.transparent)
        self.YouLostPopUp.setPalette(self.palette)
        
        self.fade.finished.connect(self.YouLostPopUp.hide)
        
        self.fade.start()
    
    def show_WordWas_popup(self):
        self.WordWasPopUp.show()
        self.WordWasPopUp.setText(f"The word was: {settings.wordchoice}")
        self.background_color = QColor(self.WordWasPopUp.palette().color(self.WordWasPopUp.backgroundRole()).rgb())
        self.fade = QPropertyAnimation(self.WordWasPopUp, b"windowOpacity")
        self.fade.setStartValue(1.0)
        self.fade.setEndValue(0.0)
        self.fade.setDuration(10000) # shows the label for 10 seconds.
        
        self.WordWasPopUp.setAutoFillBackground(True)
        self.palette = self.WordWasPopUp.palette()
        self.palette.setColor(self.WordWasPopUp.backgroundRole(), Qt.transparent)
        self.WordWasPopUp.setPalette(self.palette)
        
        self.fade.finished.connect(self.WordWasPopUp.hide)
        
        self.fade.start()
    
    def BaseGame(self):
        x = list(settings.tempstring)
        
        for i in range(len(x)):
            if x[i] in settings.wordchoice:
                if x[i] == settings.wordchoice[i]:
                    settings.boxes[settings.try_count][i].setStyleSheet(settings.rightLetterBox)
                    settings.Buttons[x[i]].setStyleSheet(settings.rightButton)
                else:
                    settings.boxes[settings.try_count][i].setStyleSheet(settings.semirightLetterBox)
                    settings.Buttons[x[i]].setStyleSheet(settings.semirightButton)
            else:
                settings.boxes[settings.try_count][i].setStyleSheet(settings.wrongLetterBox)
                settings.Buttons[x[i]].setStyleSheet(settings.wrongButton)

        # Check if game is won
        if settings.wordchoice == settings.tempstring:
            print("WINNER!!!!!!")
            scores.update_scores(1) # 1 means win
            scores.write_scores(settings.file_name, settings.Scores_dict)
            MainWindow.show_YouWon_popup(self)
            
            self.timer = QTimer()
            self.timer.timeout.connect(self.Scores)
            self.timer.singleShot(3000, self.Scores)
            
            settings.WonLost = True
            played_checker.add_record()
            print(settings.Scores_dict)
        
        # Check if game is lost
        if settings.wordchoice != settings.tempstring and settings.try_count == settings.max_letter_count:
            print("LOSER!!!!")
            scores.update_scores(0) # 0 means no win
            scores.write_scores(settings.file_name, settings.Scores_dict)
            
            MainWindow.show_YouLost_popup(self)
            
            self.timer = QTimer()
            self.timer.timeout.connect(self.Scores)
            self.timer.singleShot(3000, self.Scores)
            self.timer.singleShot(3000, self.show_WordWas_popup)
            
            settings.WonLost = True
            played_checker.add_record()
    
    def Scores(self):
        # scores.read_scores()
        Scores = StatisticsPopUp(self)
        Scores.open()
        Scores.center()
        self.dimmer.show()
        print("Scores")
        
    def HowTo(self):
        HowTo = HowToPopUp(self)
        HowTo.open()
        HowTo.center()
        self.dimmer.show()
    
                             
    def ButtonClicks(self):
        
        self.ScoresButton.clicked.connect(self.Scores)
        self.HowToButton.clicked.connect(self.HowTo)
        
        
        if settings.max_letter_count >= settings.letter_count and settings.max_try_count >= settings.try_count:
        
            Keyboard = keyboard.Keyboard(self)
            self.Test.clicked.connect(lambda: Keyboard.QButtonClicked(settings.try_count, settings.letter_count))
            self.WButton.clicked.connect(lambda: Keyboard.WButtonClicked(settings.try_count, settings.letter_count))
            self.EButton.clicked.connect(lambda: Keyboard.EButtonClicked(settings.try_count, settings.letter_count))
            self.RButton.clicked.connect(lambda: Keyboard.RButtonClicked(settings.try_count, settings.letter_count))
            self.TButton.clicked.connect(lambda: Keyboard.TButtonClicked(settings.try_count, settings.letter_count))
            self.YButton.clicked.connect(lambda: Keyboard.YButtonClicked(settings.try_count, settings.letter_count))
            self.UButton.clicked.connect(lambda: Keyboard.UButtonClicked(settings.try_count, settings.letter_count))
            self.IButton.clicked.connect(lambda: Keyboard.IButtonClicked(settings.try_count, settings.letter_count))
            self.OButton.clicked.connect(lambda: Keyboard.OButtonClicked(settings.try_count, settings.letter_count))
            self.PButton.clicked.connect(lambda: Keyboard.PButtonClicked(settings.try_count, settings.letter_count))
            self.AButton.clicked.connect(lambda: Keyboard.AButtonClicked(settings.try_count, settings.letter_count))
            self.SButton.clicked.connect(lambda: Keyboard.SButtonClicked(settings.try_count, settings.letter_count))
            self.DButton.clicked.connect(lambda: Keyboard.DButtonClicked(settings.try_count, settings.letter_count))
            self.FButton.clicked.connect(lambda: Keyboard.FButtonClicked(settings.try_count, settings.letter_count))
            self.GButton.clicked.connect(lambda: Keyboard.GButtonClicked(settings.try_count, settings.letter_count))
            self.HButton.clicked.connect(lambda: Keyboard.HButtonClicked(settings.try_count, settings.letter_count))
            self.JButton.clicked.connect(lambda: Keyboard.JButtonClicked(settings.try_count, settings.letter_count))
            self.KButton.clicked.connect(lambda: Keyboard.KButtonClicked(settings.try_count, settings.letter_count))
            self.LButton.clicked.connect(lambda: Keyboard.LButtonClicked(settings.try_count, settings.letter_count))
            self.ZButton.clicked.connect(lambda: Keyboard.ZButtonClicked(settings.try_count, settings.letter_count))
            self.XButton.clicked.connect(lambda: Keyboard.XButtonClicked(settings.try_count, settings.letter_count))
            self.CButton.clicked.connect(lambda: Keyboard.CButtonClicked(settings.try_count, settings.letter_count))
            self.VButton.clicked.connect(lambda: Keyboard.VButtonClicked(settings.try_count, settings.letter_count))
            self.BButton.clicked.connect(lambda: Keyboard.BButtonClicked(settings.try_count, settings.letter_count))
            self.NButton.clicked.connect(lambda: Keyboard.NButtonClicked(settings.try_count, settings.letter_count))
            self.MButton.clicked.connect(lambda: Keyboard.MButtonClicked(settings.try_count, settings.letter_count))
            self.ENTERButton.clicked.connect(Keyboard.ENTERButtonClicked)
            self.BACKButton.clicked.connect(lambda: Keyboard.BACKButtonClicked(settings.try_count, settings.letter_count))
            
    def keyPressEvent(self, event):
        Keyboard = keyboard.Keyboard(self)
        if not settings.WonLost:
            if event.key() == 32 and event.type() == QEvent.KeyPress: # key_Space
                Keyboard.XButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "q" or event.text() == "Q":
                Keyboard.QButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "w" or event.text() == "W":
                Keyboard.WButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "e" or event.text() == "E":
                Keyboard.EButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "r" or event.text() == "R":
                Keyboard.RButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "t" or event.text() == "T":
                Keyboard.TButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "y" or event.text() == "Y":
                Keyboard.YButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "u" or event.text() == "U":
                Keyboard.UButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "i" or event.text() == "I":
                Keyboard.IButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "o" or event.text() == "O":
                Keyboard.OButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "p" or event.text() == "P":
                Keyboard.PButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "a" or event.text() == "A":
                Keyboard.AButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "s" or event.text() == "S":
                Keyboard.SButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "d" or event.text() == "D":
                Keyboard.DButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "f" or event.text() == "F":
                Keyboard.FButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "g" or event.text() == "G":
                Keyboard.GButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "h" or event.text() == "H":
                Keyboard.HButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "j" or event.text() == "J":
                Keyboard.JButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "k" or event.text() == "K":
                Keyboard.KButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "l" or event.text() == "L":
                Keyboard.LButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "z" or event.text() == "Z":
                Keyboard.ZButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "x" or event.text() == "X":
                Keyboard.XButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "c" or event.text() == "C":
                Keyboard.CButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "v" or event.text() == "V":
                Keyboard.VButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "b" or event.text() == "B":
                Keyboard.BButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "n" or event.text() == "N":
                Keyboard.NButtonClicked(settings.try_count, settings.letter_count)
                
            if event.text() == "m" or event.text() == "M":
                Keyboard.MButtonClicked(settings.try_count, settings.letter_count)
                
            if event.key() == 16777220 or event.key() == 16777221: # Enter key on keypad and keyboard
                Keyboard.ENTERButtonClicked()
                
            if event.key() == 16777219: # key_Backspace
                Keyboard.BACKButtonClicked(settings.try_count, settings.letter_count)  


def main():
    
    # Load a random word each day 
    
    today = datetime.date.today()
    random.seed(today.year + today.month + today.day)
    settings.wordchoice = random.choice(settings.words) # choses 
    
    print(settings.wordchoice)
    
    # Initialize The App
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    
    
    mainwindow.setWindowIcon(QIcon('Assets/Wordle Clone Logo.png')) #changes the icon of the main window
    app.exec_()
    
    
if __name__ == '__main__':
    main()
