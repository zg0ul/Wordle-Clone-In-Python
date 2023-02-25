from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QDialog
from PyQt5.QtGui import QIcon, QColor
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation, QPoint
import settings
import scores

class StatisticsPopUp(QDialog):
    def __init__(self, MainWindow):
        super(StatisticsPopUp, self).__init__(MainWindow) 
        
        loadUi('Assets/Statistic.ui', self)
        self.setWindowOpacity(0)
       
        self.ExitButton.setIcon(QIcon('Assets/Icons/exit_white.png'))
        self.ExitButton.clicked.connect(self.exitPopUp)
        self.alreadyplayed.hide()
        
        self.dimmer = MainWindow.dimmer
        self.dimmer.clicked.connect(self.exitPopUp)
       
        if settings.check:
            self.alreadyplayed.show()
            self.ExitButton.setEnabled(False)
            self.ExitButton.hide()
       
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.Popup)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint )
        self.setWindowFlag(Qt.WindowTitleHint, False)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setColor(QColor(0,0,0,200))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)
        
        scores.read_scores(settings.file_name)
        self.NumPlayedLabel.setText(str(settings.Scores_dict["Number_of_games_played"]))
        self.WinPercentLabel.setText(str(settings.Scores_dict["Win_Percentage"]))
        self.CurrentStreakLabel.setText(str(settings.Scores_dict["Current_streak"]))
        self.MaxStreakLabel.setText(str(settings.Scores_dict["Max_streak"]))
        
    def center(self):
        # Keeps the Pop Up Dialog centered on the main window where ever it is.
        
        main_window = self.parent()
        dialog_rect = self.geometry()
        main_window_rect = main_window.rect()
        x = main_window_rect.x() + (main_window_rect.width() - dialog_rect.width()) / 2
        y = main_window_rect.y() + (main_window_rect.height() - dialog_rect.height()) / 2
        self.move(int(x), int(y))

    def exitPopUp(self):
        self.reject()
        self.dimmer.hide()
        
class HowToPopUp(QDialog):
    def __init__(self, MainWindow):
        super(HowToPopUp, self).__init__(MainWindow) 
        
        loadUi('Assets/HowToPlay.ui', self)
        self.setWindowOpacity(0)
       
        self.ExitButton.setIcon(QIcon('Assets/Icons/exit_white.png'))
        self.ExitButton.clicked.connect(self.exitPopUp)
        
        self.dimmer = MainWindow.dimmer
        self.dimmer.clicked.connect(self.exitPopUp)
        
        if settings.check:
            self.alreadyplayed.show()
            self.ExitButton.setEnabled(False)
            self.ExitButton.hide()
            
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.Popup)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint )
        self.setWindowFlag(Qt.WindowTitleHint, False)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setColor(QColor(0,0,0,200))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)
    
    def center(self):
        # Keeps the Pop Up Dialog centered on the main window where ever it is.
        
        main_window = self.parent()
        dialog_rect = self.geometry()
        main_window_rect = main_window.rect()
        x = main_window_rect.x() + (main_window_rect.width() - dialog_rect.width()) / 2
        y = main_window_rect.y() + (main_window_rect.height() - dialog_rect.height()) / 2
        self.move(int(x), int(y))
     
    def closeEvent(self, event):
        
        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(500)
        anim.setStartValue(self.pos())
        anim.setEndValue(self.pos() + QPoint(0, self.height()))
        anim.start()
        
        anim.finished.cnnect(lambda: super().closeEvent(event))
           
    def exitPopUp(self):
        self.reject()
        self.dimmer.hide()
       