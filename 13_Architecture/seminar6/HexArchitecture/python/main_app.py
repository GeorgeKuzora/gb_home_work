from adapters.console_printer import ConsolePrinter
from adapters.movie_reviews_repo import MovieReviewsRepo
from adapters.user_command import UserCommand
from application.movie_user import MovieUser
from domain.movie_search_request import MovieSearchRequest
from ports.i_fetch_movie_reviews import iFetchMovieReviews
from ports.i_print_movie_rewiews import iPrintMovieReviews
from ports.i_user_input import iUserInput

if __name__ == "__main__":
    fetchMovieReviews = MovieReviewsRepo()
    printMovieReviews = ConsolePrinter()

    userCommand = UserCommand(fetchMovieReviews, printMovieReviews)

    movieUser = MovieUser(userCommand)

    starWarsRequest = MovieSearchRequest("StarWars")
    starTreckRequest = MovieSearchRequest("StarTreck")

    print("Displaying reviews for movie " + starWarsRequest.getMovieName())
    movieUser.processInput(starWarsRequest)

    print("Displaying reviews for movie " + starTreckRequest.getMovieName())
    movieUser.processInput(starTreckRequest)
