
from typing import List
from domain.movie_review import MovieReview
from ports.i_print_movie_rewiews import iPrintMovieReviews


class ConsolePrinter(iPrintMovieReviews):
    def writeMovieReviews(self, movieReviewList: List[MovieReview]):
        for movieReview in movieReviewList:
          print(movieReview)






