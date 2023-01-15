"""
    Title : colorImg
    Author : GUYADER Ludovic, CARON Samuel
    Date : 22/11/2022
"""

# IMPORTS
from numpy import ndarray, zeros
from statistics import median, mean
from imgProcessing import imgProcessing

# -------------------------------------------------------
# --- class colorImg
# -------------------------------------------------------

class colorImg(imgProcessing):
    def __init__(self):
        super().__init__()

    # ---------------------- METHODS ----------------------
    def updateSizeOfImg(self, x : int, y : int):
        """ This function updates the size of the image

        Args:
            x (int): x size of the image
            y (int): y size of the image
        """
        self._x = x ; self._y = y
        for i in range(0, 3):
            self._newImg.append(zeros((x, y), dtype=float)) #type: ignore

    def calculateAverage(self, imgList : list[list[ndarray]]):
        """ This function calculates the average of the image pixels

        Args:
            imgList (list[list[np.ndarray]]): The image list

        Returns:
            np.ndarray: Returns the pixel table of the final image
        """
        i : int = 0 ; j : int = 0
        listTemporaryPixels : list[float] = []

        print("Img size = ", self._x * self._y)

        for primaryColor in range(0, len(self._newImg)):
            # Juste une ligne qui change afin de retirer les outlier. Possible de réduire le nbr de ligne en mettant un if dans for mais réduit les performances.
            if self._outlier == True :
                print("Img : Couleur | Calcul : Moyenne | Valeurs aberrantes : True")
                for i in range(0, self._x):
                    for j in range(0, self._y):
                        for img in imgList:
                            listTemporaryPixels.append(img[primaryColor][i][j])
                        listTemporaryPixels = self.outlierValue(listTemporaryPixels) # Ligne qui change
                        self._newImg[primaryColor][i][j] = mean(listTemporaryPixels)
                        listTemporaryPixels = []

            else:
                print("Img : Couleur | Calcul : Moyenne | Valeurs aberrantes : False")
                for i in range(0, self._x):
                    for j in range(0, self._y):
                        for img in imgList:
                            listTemporaryPixels.append(img[primaryColor][i][j])
                        self._newImg[primaryColor][i][j] = mean(listTemporaryPixels)
                        listTemporaryPixels = []


    def calculateMedian(self, imgList : list[list[ndarray]]):
        """ This function calculates the median of the image pixels

        Args:
            imgList (list[np.ndarray]): The image list

        Returns:
            np.ndarray: Returns the pixel table of the final image
        """
        i : int = 0 ; j : int = 0
        listTemporaryPixels : list[float] = []
        
        print("Img size = ", self._x * self._y)

        for primaryColor in range(0, len(self._newImg)):
    
            # Juste une ligne qui change afin de retirer les outlier. Possible de limiter le nbr de ligne en mettant un if dans for mais réduit les performances.
            if self._outlier == True :
                print("Img : Couleur | Calcul : Mediane | Valeurs aberrantes : True")
                for i in range(0, self._x):
                    for j in range(0, self._y):
                        for img in imgList:
                            listTemporaryPixels.append(img[primaryColor][i][j])
                        listTemporaryPixels = self.outlierValue(listTemporaryPixels) # Ligne qui change
                        self._newImg[primaryColor][i][j] = median(listTemporaryPixels)
                        listTemporaryPixels = []
            else:
                print("Img : Couleur | Calcul : Mediane | Valeurs aberrantes : False")
                for i in range(0, self._x):
                    for j in range(0, self._y):
                        for img in imgList:
                            listTemporaryPixels.append(img[primaryColor][i][j])
                        self._newImg[primaryColor][i][j] = median(listTemporaryPixels)
                        listTemporaryPixels = []
