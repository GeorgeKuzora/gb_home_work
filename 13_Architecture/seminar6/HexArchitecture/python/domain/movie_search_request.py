class MovieSearchRequest:

    def __init__(self, name):
        self.request = name


    def getMovieName(self):
        return self.request