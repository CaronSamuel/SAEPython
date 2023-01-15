"""
    Title : Model
    Author : GUYADER Ludovic, CARON Samuel
    Date : 22/11/2022
"""

# IMPORTS
from numpy import ndarray
from astropy.io import fits
import blackWhiteImg as bImg
import colorImg as cImg

# -------------------------------------------------------
# --- class Model
# -------------------------------------------------------

class Model:
    # constructor
    def __init__(self):
        self._blackWhite : bImg.blackWhiteImg = bImg.blackWhiteImg()
        self._color : cImg.colorImg = cImg.colorImg()
        
        self._file : list[str] = []

    # ---------------------- GETTER / SETTER ----------------------
    @property
    def file(self): return self._file

    @file.setter
    def file(self, filesList : list[str]): self._file = filesList

    # ---------------------- METHODS ----------------------
    def engine(self, operator : str, outlier : bool):
        """ 
        This function will call the right function to calculate the average or the median of the images

        Args:
            operator (str): The operator to use
            outlier (bool): If the user wants to remove the outlier values

        Returns:
            _type_: Returns the pixel table of the final image
        """
        imgList : list[ndarray] | list[list[ndarray]] = self.retrievePixels(self._file)

        if self.verifyDimensions(imgList):
            firstImg : ndarray | list[ndarray] = imgList[0]
            finalList : ndarray | list[ndarray]

            # Si une image est en couleur
            if (type(imgList[0]) == list):
                print("Img en couleur")
                finalList = self.engineColor(imgList, operator, outlier) # type: ignore
            else :
                print("Img sans couleur")
                finalList = self.engineUncolor(imgList, operator, outlier)

            return [firstImg, finalList]
        return None

    def engineColor(self, imgList : list[list[ndarray]], operator : str, outlier : bool):
        """
        This function will call the right function to calculate the average or the median of the images

        Args:
            imgList (list[list[ndarray]]): The list of images
            operator (str): The operator to use
            outlier (bool): If the user wants to remove the outlier values

        Returns:
            _type_: Returns the pixel table of the final image
        """
        self._color.newImg = []
        self._color.outlier = outlier
        x : int = imgList[0][0].shape[0]
        y : int = imgList[0][0].shape[1]
        print("x :", x)
        print("y :", y)
        self._color.updateSizeOfImg(x, y)
        
        if operator == "avg":
            self._color.calculateAverage(imgList)
        else :
            self._color.calculateMedian(imgList)

        return self._color.newImg

    def engineUncolor(self, imgList : list[ndarray], operator : str, outlier : bool):
        """
        This function will call the right function to calculate the average or the median of the images

        Args:
            imgList (list[ndarray]): The list of images
            operator (str): The operator to use
            outlier (bool): If the user wants to remove the outlier values

        Returns:
            _type_: Returns the pixel table of the final image
        """
        self._blackWhite.newImg = []
        self._blackWhite.outlier = outlier
        x : int = imgList[0].shape[0]
        y : int = imgList[0].shape[1]
        self._blackWhite.updateSizeOfImg(x, y)
        
        if operator == "avg":
            self._blackWhite.calculateAverage(imgList)
        else :
            self._blackWhite.calculateMedian(imgList)

        return self._blackWhite.newImg

    # @staticmethod
    def retrievePixels(self, imgList : list[str]):
        """ This function will store the pixels of the final image in the empty list imgList

        Args:
            imgList (list[str]): An empty list

        Returns:
            np.ndarray: Returns the pixel table of the final image
        """

        listImg : list[ndarray] | list[list[ndarray]] = []
        
        for elt in imgList:

            hdu_list = fits.open(elt, memmap=False)
            
            data = hdu_list[0].data # type: ignore
            image_data : ndarray | list[ndarray]

            dimensions : list[int] = data.shape

            # Si la dimensions est de taille 3, c'est un tableau en 3D --> Img en couleur
            if len(dimensions) == 3:
                image_data = [data[0], data[1], data[2]]
            else: 
                image_data = data
            hdu_list.close()
            listImg.append(image_data) # type: ignore

        return listImg

    @staticmethod
    def verifyDimensions(imgList : list[ndarray] | list[list[ndarray]]):
        """ This function allows you to check if the dimensions of the images are identical 

        Args:
            imgList (list[np.ndarray]): The image list

        Returns:
            bool: return True if the dimensions of the images are identical, else return False
        """
        # Si list[list[ndarray]] --> Recup tous les list[list[0]] et les mettres dans une list[ndarray]
        if (type(imgList[0]) == list):
            imgList = [imgList[i][0] for i in range(len(imgList))]

        lengthList : list = []
        [lengthList.append((imgList[i].shape)) for i in range(len(imgList))] # type: ignore
        
        return len(set(lengthList)) == 1