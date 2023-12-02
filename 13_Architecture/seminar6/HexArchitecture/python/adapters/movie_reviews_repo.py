from typing import List
from domain.movie_review import MovieReview
from domain.movie_search_request import MovieSearchRequest
from ports.i_fetch_movie_reviews import iFetchMovieReviews


class MovieReviewsRepo(iFetchMovieReviews):
    def __init__(self):
        self.movieReviewMap = {}
        self.initialize()


    def fetchMovieReviews(self, movieSearchRequest: MovieSearchRequest) -> List[MovieReview]:
        return self.movieReviewMap.get(movieSearchRequest.getMovieName, [])

    def initialize(self):
        self.movieReviewMap = {
            "StarWars": [MovieReview("1", 7.5, "Good")],
            "StarTreck": [MovieReview("1", 9.5, "Excellent"), MovieReview("1", 8.5, "Good")]
        }