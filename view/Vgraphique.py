"""
    Title : Vgraphique
    Author : GUYADER Ludovic, CARON Samuel
    Date : 22/11/2022
"""

# IMPORTS
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from numpy import ndarray, zeros
from astropy.visualization import make_lupton_rgb

# -------------------------------------------------------
# --- class Vgraphique
# -------------------------------------------------------

class Vgraphique(QWidget):
    
    def __init__(self, img : ndarray | list[ndarray]):
        super().__init__()

        self.figure = plt.figure() # créer une figure Canva

        # Si une image est en couleur
        if (type(img) == list):
            data_r = img[0] ; data_g = img[1] ; data_b = img[2]
            rgb_image = make_lupton_rgb(data_r, data_g, data_b)
            plt.imshow(rgb_image, cmap='jet')
        else:
            plt.imshow(img, cmap='gray')

        # afficher la figure Canva dans une fenêtre PyQt
        self.canvas = FigureCanvas(self.figure)

        self.__mainLayout : QVBoxLayout= QVBoxLayout(); self.setLayout(self.__mainLayout)

        self.__mainLayout.addWidget(self.canvas)

        self.setMinimumSize(300, 350) ; self.setMaximumSize(300, 350)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    data = zeros([5, 5], dtype=int)
    ex = Vgraphique(data)
    sys.exit(app.exec())