import random

class MovieApp:

    def __init__(self, fetchMovieReviews, printMovieReviews):
        self.fetchMovieReviews = fetchMovieReviews
        self.printMovieReviews = printMovieReviews

    def filterRandomReviews(self, movieReviewList):
        result = []
        for index in range(5):
            if len(movieReviewList) < 1:
                break
            randomIndex = self.getRandomElement(len(movieReviewList))
            movieReview = movieReviewList[randomIndex]
            movieReviewList.remove(movieReview)
            result.append(movieReview)
        return result

    def getRandomElement(self, size):
        return random.randint(0, size-1)

    def accept(self, movieSearchRequest):
        movieReviewList = self.fetchMovieReviews.fetchMovieReviews(movieSearchRequest)
        randomReviews = self.filterRandomReviews(list(movieReviewList))
        self.printMovieReviews.writeMovieReviews(randomReviews)