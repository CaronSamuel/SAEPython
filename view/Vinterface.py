"""
    Title : Vinterface
    Author : GUYADER Ludovic, CARON Samuel
    Date : 22/11/2022
"""

# IMPORTS
import sys, os
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFileDialog, QCheckBox, QGroupBox
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFont
from numpy import ndarray, zeros
import view.Vgraphique as Vg

# -------------------------------------------------------
# --- class Vgraphique
# -------------------------------------------------------
class Vinterface(QWidget):
    loadClicked = pyqtSignal(list)
    avgClicked = pyqtSignal(bool)
    medianClicked = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self.initUI()
        self._loadButton.clicked.connect(self._buttonLoad)
        self._avgButton.clicked.connect(self._buttonAvg)
        self._medianButton.clicked.connect(self._buttonMedian)

        self.show()

    def initUI(self):
        """ Create the UI """
        self._mainLayout : QVBoxLayout= QVBoxLayout(); self.setLayout(self._mainLayout)

        # ----------------------- Top LAYOUT -----------------------
        self._topLayout : QHBoxLayout = QHBoxLayout(); self._mainLayout.addLayout(self._topLayout)

        # Actions Group 
        self._actionsGroup : QGroupBox = QGroupBox("ACTIONS");self._topLayout.addWidget(self._actionsGroup)
        self._actionsLayout : QVBoxLayout = QVBoxLayout(); self._actionsGroup.setLayout(self._actionsLayout) 
        
        self._loadLayout : QHBoxLayout = QHBoxLayout(); self._actionsLayout.addLayout(self._loadLayout)
        self._loadLabel : QLabel = QLabel("Load your file : ") ; self._loadLayout.addWidget(self._loadLabel)
        self._loadButton : QPushButton = QPushButton("LOAD") ; self._loadLayout.addWidget(self._loadButton)

        # self._downloadLayout : QHBoxLayout = QHBoxLayout(); self._actionsLayout.addLayout(self._downloadLayout)
        # self._downloadLabel : QLabel = QLabel("Download your new img : ") ; self._downloadLayout.addWidget(self._downloadLabel)
        # self._downloadButton : QPushButton = QPushButton("DOWNLOAD") ; self._downloadLayout.addWidget(self._downloadButton) ; self._downloadButton.setEnabled(False)

        # Options Group
        self._optionsGroup : QGroupBox = QGroupBox("OPTIONS");self._topLayout.addWidget(self._optionsGroup)
        self._optionsLayout : QVBoxLayout = QVBoxLayout(); self._optionsGroup.setLayout(self._optionsLayout) 

        self._outlierLayout : QHBoxLayout = QHBoxLayout(); self._optionsLayout.addLayout(self._outlierLayout)
        self._outlierLabel : QLabel = QLabel("Do you want img with outlier values : ") ; self._outlierLayout.addWidget(self._outlierLabel)
        self._outlierCheckBox : QCheckBox = QCheckBox(); self._outlierLayout.addWidget(self._outlierCheckBox)

        # Stacking methods Group
        self._stackingGroup : QGroupBox = QGroupBox("STACKING METHODS");self._topLayout.addWidget(self._stackingGroup)
        self._stackingLayout : QVBoxLayout = QVBoxLayout(); self._stackingGroup.setLayout(self._stackingLayout) 

        self._avgButton : QPushButton = QPushButton("AVERAGE METHOD") ; self._stackingLayout.addWidget(self._avgButton) ; self._avgButton.setEnabled(False)
        self._medianButton : QPushButton = QPushButton("MEDIAN METHOD") ; self._stackingLayout.addWidget(self._medianButton) ; self._medianButton.setEnabled(False)


        # ----------------------- Bottom LAYOUT -----------------------
        self._bottomLayout = QHBoxLayout() ; self._mainLayout.addLayout(self._bottomLayout)
        
        # Left Graphic 
        self._leftLayout = QVBoxLayout() ; self._bottomLayout.addLayout(self._leftLayout)
        self._titleLeftGraphique = QLabel() ; self._leftLayout.addWidget(self._titleLeftGraphique)
        self._titleLeftGraphique.setFont(QFont('Arial', 15)) ; self._titleLeftGraphique.setText("Before (first img of the directory) : ")
        self._graphiqueLeft : Vg.Vgraphique = Vg.Vgraphique(zeros([1, 1], dtype=int)) ; 

        
        # Right Graphic 
        self._rightLayout = QVBoxLayout() ; self._bottomLayout.addLayout(self._rightLayout)
        self._titleRightGraphique = QLabel() ; self._rightLayout.addWidget(self._titleRightGraphique)
        self._titleRightGraphique.setFont(QFont('Arial', 15)) ; self._titleRightGraphique.setText("After : ")
        self._graphiqueRight : Vg.Vgraphique = Vg.Vgraphique(zeros([5, 5], dtype=int)) ; 


    def _buttonLoad(self):
        """ Load the files in the directory """
        list_of_files : list[str] = []
        try:
            path = QFileDialog.getExistingDirectory(None, 'Open working directory')
            if path != "":
                for root, directories, files in os.walk(path):
                    for file in files:
                        if(file.endswith(".fits") or file.endswith(".fit")):
                            list_of_files.append(os.path.join(root,file))
        except FileNotFoundError:
            pass
        
        if list_of_files != []:
            self._avgButton.setEnabled(True)
            self._medianButton.setEnabled(True)
            self.loadClicked.emit(list_of_files)
        else:
            self._avgButton.setEnabled(False)
            self._medianButton.setEnabled(False)


    def _buttonAvg(self): self.avgClicked.emit(self._outlierCheckBox.isChecked())

    def _buttonMedian(self): self.medianClicked.emit(self._outlierCheckBox.isChecked())
    
    def showImagesToGraphique(self, firstImg : ndarray | list[ndarray], lastImg : ndarray | list[ndarray]):
        """ 
        This function is used to show the images in the graphique

        Args:
            firstImg (ndarray | list[ndarray]): the first image of the directory
            lastImg (ndarray | list[ndarray]): the last image of the directory
        """
        self._graphiqueLeft.deleteLater() ; self._graphiqueRight.deleteLater()
        self._graphiqueLeft : Vg.Vgraphique = Vg.Vgraphique(firstImg) ; self._leftLayout.addWidget(self._graphiqueLeft) ; self._graphiqueLeft.show()

        self._graphiqueRight : Vg.Vgraphique = Vg.Vgraphique(lastImg) ; self._rightLayout.addWidget(self._graphiqueRight) ; self._graphiqueRight.show()

        self.setMinimumSize(646, 497) ; self.setMaximumSize(646, 497)
        
        print("PHOTO A JOUR")
        print("---------------  ---------------")

if __name__ == '_main_':
    app = QApplication(sys.argv)
    ex = Vinterface()
    sys.exit(app.exec())