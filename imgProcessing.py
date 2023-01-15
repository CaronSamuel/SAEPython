"""
    Title : imgProcessing
    Author : GUYADER Ludovic, CARON Samuel
    Date : 22/11/2022
"""

# IMPORTS
from numpy import ndarray, percentile
from abc import abstractmethod

# import à supp
# import time
# start = time.time()
        
# end = time.time()
# # show time of execution per iteration
# print(end-start)

# -------------------------------------------------------
# --- class imgProcessing
# -------------------------------------------------------

class imgProcessing():
    def __init__(self):
        self._outlier : bool = False

        self._x : int = 1
        self._y : int = 1

        self._newImg : ndarray | list[ndarray] = []

    # ---------------------- GETTER / SETTER ----------------------
    @property
    def outlier(self): return self._outlier
    
    @outlier.setter
    def outlier(self, outlier : bool): self._outlier = outlier

    @property
    def x(self): return self._x
    
    @x.setter
    def x(self, x : bool): self._x = x
    
    @property
    def y(self): return self._y
    
    @y.setter
    def y(self, y : bool): self._y = y
    
    @property
    def newImg(self): return self._newImg
    
    @newImg.setter
    def newImg(self, newImg : list): self._newImg = newImg
    
    # ---------------------- METHODS ----------------------
    @abstractmethod
    def updateSizeOfImg(self, x : int, y : int):
        pass

    @abstractmethod
    def calculateAverage(self):
        """ This function calculates the average of the image pixels
        
        Returns:
            np.ndarray: Returns the pixel table of the final image
        """
        pass

    @abstractmethod
    def calculateMedian(self):
        """ This function calculates the median of the image pixels

        Returns:
            np.ndarray: Returns the pixel table of the final image
        """
        pass

    @staticmethod
    def outlierValue(pixels : list[float] | list[int]):
        """
        This function removes the outlier values from a list of pixels

        Args:
            pixels (list[float] | list[int]): The list of pixels

        Returns:
            _type_: Returns the list of pixels without the outlier values
        """
        q1 : float = float(percentile(pixels, 25))
        q3 : float = float(percentile(pixels, 75))
        iqr : float = q3 - q1
        
        thresholdMin = q1 - 1.5 * iqr
        thresholdMax =  q3 + 1.5 * iqr

        withoutOutlier : list[float] | list[int] = []
        for i in pixels:
            if i >= thresholdMin and i <= thresholdMax :
                withoutOutlier.append(i)

        return withoutOutlier