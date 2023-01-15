"""
    Title : blackWhiteImg
    Author : GUYADER Ludovic, CARON Samuel
    Date : 22/11/2022
"""

# IMPORTS
from statistics import median, mean
from numpy import ndarray, zeros
from imgProcessing import imgProcessing

# -------------------------------------------------------
# --- class blackWhiteImg
# -------------------------------------------------------

class blackWhiteImg(imgProcessing):
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
        self._newImg = zeros((x, y), dtype=int)

    def calculateAverage(self, imgList : list[ndarray]):
        """ 
        This function calculates the average of the image pixels

        Args:
            imgList (list[np.ndarray]): The image list

        Returns:
            np.ndarray: Returns the pixel table of the final image
        """
        i : int = 0 ; j : int = 0
        listTemporary : list[int] = []

        print("Img size = ", self.x * self._y)

        # Juste une ligne qui change afin de retirer les outlier. Possible de limiter le nbr de ligne en mettant un if dans for mais réduit les performances.
        if self._outlier == True : # Calcule sans les valeurs aberrantes 
            print("Img : Noir & blanc | Calcul : Moyenne | Valeurs aberrantes : True")
            for i in range(0, self.x):
                for j in range(0, self._y):
                    for img in imgList:
                        listTemporary.append(img[i][j])
                    listTemporary = self.outlierValue(listTemporary) # type: ignore
                    self._newImg[i][j] = mean(listTemporary)
                    listTemporary = []
        else:
            print("Img : Noir & blanc | Calcul : Moyenne | Valeurs aberrantes : False")
            for i in range(0, self.x):
                for j in range(0, self._y):
                    for img in imgList:
                        listTemporary.append(img[i][j])
                    self._newImg[i][j] = mean(listTemporary)
                    listTemporary = []
        return
    
    def calculateMedian(self, imgList : list[ndarray]):
        """ This function calculates the median of the image pixels

        Args:
            imgList (list[np.ndarray]): The image list

        Returns:
            np.ndarray: Returns the pixel table of the final image
        """
        i : int = 0 ; j : int = 0
        listTemporary : list[int] = []
        
        print("Img size = ", self._x * self._y)
        
        # Juste une ligne qui change afin de retirer les outlier. Possible de limiter le nbr de ligne en mettant un if dans for mais réduit les performances.
        if self._outlier == True :
            print("Img : Noir & blanc | Calcul : Médiane | Valeurs aberrantes : True")
            for i in range(0, self._x):
                for j in range(0, self._y):
                    for img in imgList:
                        listTemporary.append(img[i][j])
                    listTemporary = self.outlierValue(listTemporary) # type: ignore
                    self._newImg[i][j] = median(listTemporary)
                    listTemporary = []
        else:
            print("Img : Noir & blanc | Calcul : Médiane | Valeurs aberrantes : False")
            for i in range(0, self._x):
                for j in range(0, self._y):
                    for img in imgList:
                        listTemporary.append(img[i][j])
                    self._newImg[i][j] = median(listTemporary)
                    listTemporary = []
        return