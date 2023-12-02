from application.movie_app import MovieApp
from domain.model import Model
from ports.i_fetch_movie_reviews import iFetchMovieReviews
from ports.i_print_movie_rewiews import iPrintMovieReviews
from ports.i_user_input import iUserInput


class UserCommand(iUserInput):
    def __init__(self, fetchMovieReviews: iFetchMovieReviews, printMovieReviews: iPrintMovieReviews):
        movieApp = MovieApp(fetchMovieReviews, printMovieReviews)
        self.model = Model(movieApp)


    def handleUserInput(self, userCommand):
        self.model.Run(userCommand)