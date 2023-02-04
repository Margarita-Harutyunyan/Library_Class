class Book:
    def __init__(self, title, pageNumber):
        self.__title = title
        self.__pageNumber = pageNumber
    
    def setTitle(self, Title):
        self.__title = Title
    def getTitle(self):
        return self.__title

    def setPageNumber(self, pageNumber):
        self.__pageNumber = pageNumber
    def getPageNumber(self):
        return self.__pageNumber
