"""
    Title : Controller
    Author : GUYADER Ludovic, CARON Samuel
    Date : 22/11/2022
"""

# IMPORTS
import sys
from PyQt6.QtWidgets import QApplication
import Model as model
import view.Vinterface as v
from numpy import ndarray

# -------------------------------------------------------
# --- class Controller
# -------------------------------------------------------

class Controller:
    # constructor
    def __init__(self):
        self.__model : model.Model = model.Model()
        self.__view : v.Vinterface = v.Vinterface()

        # Callback
        self.__view.loadClicked.connect(self.loadFunction)
        self.__view.avgClicked.connect(self.avgFunction)
        self.__view.medianClicked.connect(self.medianFunction)

    def loadFunction(self, pathList : list[str]): 
        """ 
        This function loads the images

        Args:
            pathList (list[str]): The path list of the images
        """
        self.__model.file = pathList

    def avgFunction(self, outlier : bool):
        """ 
        This function calculates the average of the images

        Args:
            outlier (bool): True if you want to remove the outlier
        """
        firstImg : ndarray | list[ndarray]
        lastImg : ndarray | list[ndarray]
        
        temp = self.__model.engine("avg", outlier)
        if type(temp) != None:
            firstImg = temp[0]  # type: ignore
            lastImg = temp[1] # type: ignore
            
            self.__view.showImagesToGraphique(firstImg, lastImg) # type: ignore
        else :
            print("Erreur : Les dimensions de vos images ne sont pas équivalentes")

    def medianFunction(self, outlier : bool):
        """ 
        This function calculates the median of the images

        Args:
            outlier (bool): True if you want to remove the outlier
        """
        firstImg : ndarray | list[ndarray]
        lastImg : ndarray | list[ndarray]

        temp = self.__model.engine("median", outlier)
        if type(temp) != None:
            firstImg = temp[0]  # type: ignore
            lastImg = temp[1] # type: ignore
            
            self.__view.showImagesToGraphique(firstImg, lastImg) # type: ignore
        else :
            print("Erreur : Les dimensions de vos images ne sont pas équivalentes")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Controller()
    sys.exit(app.exec())
