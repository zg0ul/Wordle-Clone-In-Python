import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import QPropertyAnimation, QMargins, QEasingCurve
import settings
from PyQt5.Qt import Qt
from main import MainWindow


class Keyboard(QMainWindow):
    def __init__(self, main):
        super().__init__(main)

        self.notwordpopup = main.notwordpopup
        self.noletterspopup = main.noletterspopup
        self.YouWonPopUp = main.YouWonPopUp
        self.YouLostPopUp = main.YouLostPopUp
        self.WordWasPopUp = main.WordWasPopUp
        self.dimmer = main.dimmer
        self.Scores = main.Scores
        self.show_WordWas_popup = main.show_WordWas_popup
        
    def WButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("W")
            settings.tempstring += "W"
            settings.letter_count += 1
        
    def QButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("Q")
            settings.tempstring += "Q"
            settings.letter_count += 1
    
    def EButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("E")
            settings.tempstring += "E"
            settings.letter_count += 1
        
    def RButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("R")
            settings.tempstring += "R"
            settings.letter_count += 1
        
    def TButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("T")
            settings.tempstring += "T"
            settings.letter_count += 1
        
    def YButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("Y")
            settings.tempstring += "Y"
            settings.letter_count += 1
        
    def UButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("U")
            settings.tempstring += "U"
            settings.letter_count += 1
        
    def IButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("I")
            settings.tempstring += "I"
            settings.letter_count += 1
        
    def OButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("O")
            settings.tempstring += "O"
            settings.letter_count += 1
        
    def PButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("P")
            settings.tempstring += "P"
            settings.letter_count += 1
        
    def AButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("A")
            settings.tempstring += "A"
            settings.letter_count += 1
        
    def SButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("S")
            settings.tempstring += "S"
            settings.letter_count += 1
        
    def DButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("D")
            settings.tempstring += "D"
            settings.letter_count += 1
            
    def FButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("F")
            settings.tempstring += "F"
            settings.letter_count += 1
        
    def GButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("G")
            settings.tempstring += "G"
            settings.letter_count += 1
        
    def HButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("H")
            settings.tempstring += "H"
            settings.letter_count += 1
        
    def JButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("J")
            settings.tempstring += "J"
            settings.letter_count += 1
        
    def KButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("K")
            settings.tempstring += "K"
            settings.letter_count += 1
        
    def LButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("L")
            settings.tempstring += "L"
            settings.letter_count += 1
        
    def ZButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("Z")
            settings.tempstring += "Z"
            settings.letter_count += 1
        
    def XButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("X")
            settings.tempstring += "X"
            settings.letter_count += 1
        
    def CButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("C")
            settings.tempstring += "C"
            settings.letter_count += 1
        
    def VButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("V")
            settings.tempstring += "V"
            settings.letter_count += 1
        
    def BButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("B")
            settings.tempstring += "B"
            settings.letter_count += 1
        
    def NButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("N")
            settings.tempstring += "N"
            settings.letter_count += 1
        
    def MButtonClicked(self, i, j):
        if settings.letter_count != settings.max_letter_count:
            settings.boxes[i][j].setStyleSheet(settings.FilledBox)
            settings.boxes[i][j].setText("M")
            settings.tempstring += "M"
            settings.letter_count += 1
                
    def ENTERButtonClicked(self):
        # print("Enter")
        
        if settings.letter_count == settings.max_letter_count:
            settings.tempstring = settings.tempstring.lower()
            if settings.tempstring in settings.words:
                print(settings.tempstring)
                MainWindow.BaseGame(self)
                settings.letter_count = 0
                settings.try_count += 1
                settings.tempstring = ""

            else:
                MainWindow.show_nowords_popup(self)
        
        else:
            MainWindow.show_noletters_popup(self)      
    
    def BACKButtonClicked(self, i, j):
        if settings.letter_count != 0:
            settings.boxes[i][j-1].setStyleSheet(settings.DefaultBox)
            settings.boxes[i][j-1].setText("")
            settings.tempstring = settings.tempstring.rstrip(settings.tempstring[-1])
            settings.letter_count -= 1
 

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Keyboard = Keyboard()
    sys.exit(App.exec_())