class Model:

    def __init__(self, movieApp):
        self.movieApp = movieApp


    def Run(self, userCommand):
        self.movieApp.accept(userCommand)


