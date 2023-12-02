class MovieReview:
 
    def __init__(self, movieName, movieScore, remark):
        self.movieName = movieName
        self.movieScore = movieScore
        self.remark = remark

    def __str__(self):
        return " " + str(self.movieScore) + " " + self.remark